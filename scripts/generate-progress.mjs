#!/usr/bin/env node

/**
 * Build the repository-owned progress.json bridge contract.
 *
 * The contract deliberately contains facts only: solutions, source hashes, artifact
 * availability, and git-derived solve history. Curriculum decisions stay in the
 * Playbook repository.
 */
import { createHash } from "node:crypto";
import { execFileSync } from "node:child_process";
import {
  existsSync,
  readFileSync,
  readdirSync,
  statSync,
  writeFileSync,
} from "node:fs";
import { dirname, extname, join, relative, resolve, sep } from "node:path";
import { fileURLToPath } from "node:url";

export const SCHEMA_VERSION = "1.0.0";
export const REPOSITORY_URL = "https://github.com/RaghhavMalani/leetcode-progress";

const SCRIPT_DIR = dirname(fileURLToPath(import.meta.url));
const DEFAULT_ROOT = resolve(SCRIPT_DIR, "..");
const SOLUTION_LANGUAGES = Object.freeze({
  ".c": "c",
  ".cpp": "cpp",
  ".java": "java",
  ".js": "js",
  ".py": "py",
});

const SEP = String.raw`\s*(?:&nbsp;)?\s*(?:&middot;|&#183;|·)\s*(?:&nbsp;)?\s*`;
const NOTES_HEADER = new RegExp(
  String.raw`>\s*\*\*(\w+)\*\*` +
    SEP +
    String.raw`(.*?)` +
    SEP +
    String.raw`family:\s*\*\*(.*?)\*\*`,
);
const DIFFICULTY_ONLY = />\s*\*\*(\w+)\*\*/;

function toRepoPath(root, path) {
  return relative(root, path).split(sep).join("/");
}

function git(root, args, fallback = "") {
  try {
    return execFileSync("git", ["-C", root, ...args], {
      encoding: "utf8",
      maxBuffer: 32 * 1024 * 1024,
      stdio: ["ignore", "pipe", "pipe"],
    }).trim();
  } catch {
    return fallback;
  }
}

function parseNotes(path) {
  if (!existsSync(path)) return { difficulty: "", label: "", family: "" };
  const text = readFileSync(path, "utf8");
  const header = NOTES_HEADER.exec(text);
  if (header) {
    return {
      difficulty: header[1].toLowerCase(),
      label: header[2],
      family: header[3],
    };
  }
  const difficulty = DIFFICULTY_ONLY.exec(text)?.[1]?.toLowerCase() ?? "";
  return { difficulty, label: "", family: "" };
}

function findTrace(root, directory) {
  const candidates = [
    join(root, "visualizations", `${directory}.html`),
    join(root, "visualizations", `${directory}.auto.html`),
    join(root, directory, "visualization.html"),
  ];
  return candidates.find(existsSync) ?? null;
}

function hashFile(path) {
  return createHash("sha256").update(readFileSync(path)).digest("hex");
}

/** Return solution-touching commits, oldest first, grouped by problem directory. */
function solutionHistory(root, sourceCommit, problemDirectories) {
  const byDirectory = new Map([...problemDirectories].map((directory) => [directory, []]));
  const raw = git(
    root,
    [
      "log",
      sourceCommit,
      "--format=%x1e%H%x1f%aI",
      "--name-only",
      "--diff-filter=AMR",
      "--",
    ],
  );

  for (const record of raw.split("\x1e")) {
    const lines = record
      .split(/\r?\n/)
      .map((line) => line.trim())
      .filter(Boolean);
    if (!lines.length) continue;

    const [commit, solvedAt] = lines.shift().split("\x1f");
    if (!/^[a-f0-9]{40}$/.test(commit ?? "") || Number.isNaN(Date.parse(solvedAt ?? ""))) continue;

    const languagesByDirectory = new Map();
    for (const path of lines) {
      const normalized = path.replaceAll("\\", "/");
      const slash = normalized.indexOf("/");
      if (slash < 0) continue;
      const directory = normalized.slice(0, slash);
      if (!byDirectory.has(directory)) continue;
      const language = SOLUTION_LANGUAGES[extname(normalized).toLowerCase()];
      if (!language || normalized.slice(slash + 1).includes("/")) continue;
      const languages = languagesByDirectory.get(directory) ?? new Set();
      languages.add(language);
      languagesByDirectory.set(directory, languages);
    }

    for (const [directory, languages] of languagesByDirectory) {
      byDirectory.get(directory).push({
        sourceCommit: commit,
        solvedAt,
        languages: [...languages].sort(),
      });
    }
  }

  for (const history of byDirectory.values()) {
    history.sort(
      (a, b) => Date.parse(a.solvedAt) - Date.parse(b.solvedAt) || a.sourceCommit.localeCompare(b.sourceCommit),
    );
  }
  return byDirectory;
}

function readDeclaredStats(root) {
  const path = join(root, "stats.json");
  if (!existsSync(path)) return null;
  try {
    const stats = JSON.parse(readFileSync(path, "utf8")).leetcode;
    if (!stats) return null;
    return {
      solved: Number.isInteger(stats.solved) ? stats.solved : null,
      easy: Number.isInteger(stats.easy) ? stats.easy : null,
      medium: Number.isInteger(stats.medium) ? stats.medium : null,
      hard: Number.isInteger(stats.hard) ? stats.hard : null,
    };
  } catch {
    return null;
  }
}

export function validateProgressContract(contract) {
  const fail = (message) => {
    throw new Error(`[progress-contract] ${message}`);
  };
  if (contract?.schemaVersion !== SCHEMA_VERSION) fail(`expected schemaVersion ${SCHEMA_VERSION}`);
  if (Number.isNaN(Date.parse(contract.generatedAt))) fail("generatedAt must be an ISO timestamp");
  if (!/^[a-f0-9]{40}$/.test(contract.sourceCommit)) fail("sourceCommit must be a full git SHA");
  if (!Array.isArray(contract.problems)) fail("problems must be an array");

  const numbers = new Set();
  for (const problem of contract.problems) {
    if (!Number.isInteger(problem.number) || problem.number <= 0) fail("problem number must be positive");
    if (numbers.has(problem.number)) fail(`duplicate problem number ${problem.number}`);
    numbers.add(problem.number);
    if (!/^\d{4}-[a-z0-9-]+$/.test(problem.directory)) fail(`invalid directory ${problem.directory}`);
    if (!["", "easy", "medium", "hard"].includes(problem.difficulty)) {
      fail(`${problem.directory} has invalid difficulty ${JSON.stringify(problem.difficulty)}`);
    }
    if (!Array.isArray(problem.languages) || problem.languages.length === 0) {
      fail(`${problem.directory} has no solution language`);
    }
    if (!problem.artifacts || typeof problem.artifacts.notes?.available !== "boolean") {
      fail(`${problem.directory} has invalid artifact availability`);
    }
    if (typeof problem.artifacts.trace?.available !== "boolean") {
      fail(`${problem.directory} has invalid trace availability`);
    }
    const hashes = Object.entries(problem.solutionHashes ?? {});
    if (!hashes.length) fail(`${problem.directory} has no solution hashes`);
    for (const [path, hash] of hashes) {
      if (!path.startsWith(`${problem.directory}/`) || !/^[a-f0-9]{64}$/.test(hash)) {
        fail(`${problem.directory} has invalid solution hash for ${path}`);
      }
    }
    if (Number.isNaN(Date.parse(problem.lastSolvedAt))) {
      fail(`${problem.directory} has invalid lastSolvedAt`);
    }
    if (!Array.isArray(problem.reSolveHistory)) fail(`${problem.directory} has invalid reSolveHistory`);
    for (const event of problem.reSolveHistory) {
      if (
        !/^[a-f0-9]{40}$/.test(event.sourceCommit ?? "") ||
        Number.isNaN(Date.parse(event.solvedAt)) ||
        !Array.isArray(event.languages) ||
        event.languages.length === 0
      ) {
        fail(`${problem.directory} has an invalid re-solve event`);
      }
    }
  }
  return contract;
}

export function generateProgressContract({
  root = DEFAULT_ROOT,
  generatedAt = new Date().toISOString(),
  sourceCommit,
} = {}) {
  root = resolve(root);
  sourceCommit = sourceCommit ?? git(root, ["rev-parse", "HEAD"]);
  if (!/^[a-f0-9]{40}$/.test(sourceCommit)) {
    throw new Error("[progress-contract] could not resolve a full source commit");
  }

  const scanned = [];
  for (const directory of readdirSync(root).sort()) {
    const problemPath = join(root, directory);
    if (!/^\d{4}-[a-z0-9-]+$/.test(directory) || !statSync(problemPath).isDirectory()) continue;
    const solutions = readdirSync(problemPath)
      .filter((name) => SOLUTION_LANGUAGES[extname(name).toLowerCase()])
      .sort()
      .map((name) => ({
        absolutePath: join(problemPath, name),
        path: `${directory}/${name}`,
        language: SOLUTION_LANGUAGES[extname(name).toLowerCase()],
      }));
    // A LeetHub README or an unfinished NOTES.md is an attempt, not a solved problem.
    if (!solutions.length) continue;
    scanned.push({ directory, problemPath, solutions });
  }

  const histories = solutionHistory(root, sourceCommit, new Set(scanned.map(({ directory }) => directory)));
  const problems = scanned.map(({ directory, problemPath, solutions }) => {
    const number = Number.parseInt(directory.slice(0, 4), 10);
    const notesPath = join(problemPath, "NOTES.md");
    const tracePath = findTrace(root, directory);
    const classification = parseNotes(notesPath);
    const history = histories.get(directory) ?? [];
    const fileFallback = solutions
      .map(({ absolutePath }) => statSync(absolutePath).mtime)
      .sort((a, b) => a.getTime() - b.getTime());
    const firstSolvedAt = history[0]?.solvedAt ?? fileFallback[0].toISOString();
    const lastSolvedAt = history.at(-1)?.solvedAt ?? fileFallback.at(-1).toISOString();

    return {
      number,
      slug: directory.slice(5),
      directory,
      difficulty: classification.difficulty,
      classification: {
        label: classification.label,
        family: classification.family,
      },
      languages: [...new Set(solutions.map(({ language }) => language))].sort(),
      artifacts: {
        notes: {
          available: existsSync(notesPath),
          path: existsSync(notesPath) ? toRepoPath(root, notesPath) : null,
        },
        trace: {
          available: Boolean(tracePath),
          path: tracePath ? toRepoPath(root, tracePath) : null,
        },
      },
      solutionHashes: Object.fromEntries(
        solutions.map(({ absolutePath, path }) => [path, hashFile(absolutePath)]),
      ),
      firstSolvedAt,
      lastSolvedAt,
      // The first solution commit is the initial solve; later solution commits are re-solves.
      reSolveHistory: history.slice(1),
    };
  });

  return validateProgressContract({
    schemaVersion: SCHEMA_VERSION,
    generatedAt: new Date(generatedAt).toISOString(),
    sourceCommit,
    repository: REPOSITORY_URL,
    declaredStats: readDeclaredStats(root),
    problems,
  });
}

function parseArgs(argv) {
  const options = { root: DEFAULT_ROOT, output: join(DEFAULT_ROOT, "progress.json"), stdout: false };
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    if (arg === "--root") options.root = resolve(argv[++i]);
    else if (arg === "--output") options.output = resolve(argv[++i]);
    else if (arg === "--source-commit") options.sourceCommit = argv[++i];
    else if (arg === "--generated-at") options.generatedAt = argv[++i];
    else if (arg === "--stdout") options.stdout = true;
    else throw new Error(`[progress-contract] unknown argument: ${arg}`);
  }
  return options;
}

const invokedPath = process.argv[1] ? resolve(process.argv[1]) : "";
if (invokedPath === fileURLToPath(import.meta.url)) {
  const options = parseArgs(process.argv.slice(2));
  const contract = generateProgressContract(options);
  if (options.stdout) {
    process.stdout.write(JSON.stringify(contract));
  } else {
    writeFileSync(options.output, `${JSON.stringify(contract, null, 2)}\n`, "utf8");
    console.log(
      `[progress-contract] ${contract.problems.length} solved problems at ${contract.sourceCommit.slice(0, 7)} ` +
        `→ ${options.output}`,
    );
  }
}
