# Playbook progress bridge

This repository owns the solution facts consumed by
[PLAYBOOK-theDSAEngine](https://github.com/RaghhavMalani/PLAYBOOK-theDSAEngine).
The boundary is `progress.json`, a versioned contract validated by
`progress.schema.json`.

The contract contains only repository facts:

- the exact source commit and generation timestamp;
- solution languages and SHA-256 hashes;
- notes and replay-trace availability;
- first/last solved timestamps and git-derived re-solve history; and
- the classification recorded in each problem's `NOTES.md`.

Curriculum mapping, mastery rules, recommendations, and UI stay in Playbook.

## Publishing loop

`.github/workflows/publish-progress.yml` runs after each non-bot push to `main`
or `master`:

1. Check out the full git history.
2. Regenerate and validate `progress.json` from the solution directories,
   `NOTES.md` files, traces, and commit history.
3. Commit the contract as `github-actions[bot]`.
4. Send a `progress-updated` repository dispatch to Playbook.

The bot-authored contract push is ignored by the workflow, preventing a loop.
Playbook's strict `sync-progress.yml` job then imports the published contract,
regenerates its committed snapshot and replay data, runs its verification suite,
and commits only when the imported state changed.

## One-time repository setup

Create a fine-grained repository secret named `PLAYBOOK_REPO_TOKEN` in this
repository. Scope it to `RaghhavMalani/PLAYBOOK-theDSAEngine` with repository
**Contents: read and write** so it can create the repository dispatch.

The repository's Actions settings must also allow `GITHUB_TOKEN` to write
contents, because the publishing workflow commits `progress.json` back to the
current branch.

## Local verification

```bash
node scripts/generate-progress.mjs
node scripts/generate-progress.mjs --stdout > tmp.json
```

For reproducible checks, pass both provenance fields explicitly:

```bash
node scripts/generate-progress.mjs \
  --source-commit <full-commit-sha> \
  --generated-at <iso-8601-timestamp> \
  --output progress.verify.json
```

Given the same repository state, source commit, and timestamp, generation is
byte-for-byte deterministic.
