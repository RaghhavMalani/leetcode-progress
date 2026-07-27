# visualizations/

One traced, interactive page per solved problem, plus the shared engine that renders them.

| File | What it is |
|---|---|
| `index.html` | **Start here.** All 109 problems grouped by pattern family, with a live filter. |
| `<problem-slug>.html` | One problem: your source with the executing line highlighted, the data structures drawn as they change, a narration for every step, and the full theory section below. |
| `_engine.css` / `_engine.js` | The shared step-player and the view renderers (array, bars, hash map, stack, linked list, grid, recursion tree, binary tree, call stack). |
| `_mk.py` | Build helper — wraps a per-problem spec into a page and injects the **real** source straight from the problem folder, so a page can never drift from the code it claims to trace. |
| `_check.py` | Verifier — runs every page headlessly, replays its trace, and asserts that every step points at a line that exists and carries narration. Run `python3 _check.py`. |
| `_index.json` / `_groups.json` | Extracted metadata used to generate `index.html`, `../PATTERNS.md` and every `NOTES.md`. |

## Controls

**← →** step · **space** play/pause · drag the scrubber · *Skip to next …* jumps to the next milestone
(answer found, record beaten, pop, merge — whatever matters for that problem).

## Regenerating

Pages embed the source at build time. If you edit a solution, rebuild that page so the trace matches:

```bash
cd visualizations
python3 _check.py            # verify every page still builds and every line number is valid
```

Everything is plain static HTML — no build step, no dependencies, no network. Open any file directly.
