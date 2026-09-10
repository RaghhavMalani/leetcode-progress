import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { dirname, resolve } from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";
import {
  generateProgressContract,
  validateProgressContract,
} from "./generate-progress.mjs";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const SOURCE_COMMIT = execFileSync("git", ["-C", ROOT, "rev-parse", "HEAD"], {
  encoding: "utf8",
}).trim();
const GENERATED_AT = "2026-01-01T00:00:00.000Z";

test("generation is deterministic for fixed provenance", () => {
  const first = generateProgressContract({
    root: ROOT,
    sourceCommit: SOURCE_COMMIT,
    generatedAt: GENERATED_AT,
  });
  const second = generateProgressContract({
    root: ROOT,
    sourceCommit: SOURCE_COMMIT,
    generatedAt: GENERATED_AT,
  });

  assert.deepEqual(second, first);
  assert.equal(first.sourceCommit, SOURCE_COMMIT);
  assert.equal(first.generatedAt, GENERATED_AT);
  assert.ok(first.problems.length > 100);
  assert.deepEqual(
    first.problems.map(({ number }) => number),
    [...first.problems.map(({ number }) => number)].sort((a, b) => a - b),
  );
});

test("validation rejects malformed provenance and duplicate problems", () => {
  const contract = generateProgressContract({
    root: ROOT,
    sourceCommit: SOURCE_COMMIT,
    generatedAt: GENERATED_AT,
  });

  assert.throws(
    () => validateProgressContract({ ...contract, sourceCommit: "short" }),
    /sourceCommit must be a full git SHA/,
  );
  assert.throws(
    () => validateProgressContract({
      ...contract,
      problems: [contract.problems[0], contract.problems[0]],
    }),
    /duplicate problem number/,
  );
});
