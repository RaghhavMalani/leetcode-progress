# 36. Valid Sudoku
> **Medium** &nbsp;&middot;&nbsp; Hash sets · index-to-bucket mapping &nbsp;&middot;&nbsp; family: **Hashing**

The whole problem is one expression: `(row//3, col//3)`. That maps a cell to its 3×3 box, which turns three different geometric constraints into three identical set lookups.

**▶ [Step through this solution line by line](./visualization.html)** — 28 steps, traced on `the LeetCode example 2 board (invalid)`.

| | |
|---|---|
| time | O(81) = O(1) for a fixed board; O(n²) for an n×n generalisation |
| space | O(1) / O(n²) |

## The idea

When several constraints have different *shapes*, find a **key function** that reduces each to the same operation. Row is keyed by `r`, column by `c`, box by `(r//3, c//3)` — and then all three are just "is this value already in that set?". Integer division as a bucketing function is worth remembering on its own.

## How to recognise it

- Grid problems with block/region constraints — sudoku, chunked matrices, tiling.
- More generally: whenever you need to group by a coarser coordinate, `index // block_size` is the mapping.
- Doing three separate passes (one for rows, one for columns, one for boxes) is also correct; doing all three in a single pass is tidier and shows you saw the unification.

## Where people go wrong

- **Getting the box key wrong.** `(r//3)*3 + c//3` and `(r//3, c//3)` both work; `r//3 + c//3` does NOT — it collides boxes (0,1) and (1,0).
- **Forgetting to skip "."**. Empty cells would collide with each other instantly.
- **Validating solvability instead of validity.** The question only asks whether the current board breaks a rule — not whether it can be completed. That is LC 37 and it is a much harder backtracking problem.
- **Using `defaultdict(set)` and then indexing it in a membership test** — `rows[row]` creates an empty set as a side effect. Harmless here, but a real memory leak in long-running code.

## The reusable template

```python
# Three constraints, one operation - the key function does the work
rows = defaultdict(set); cols = defaultdict(set); boxes = defaultdict(set)

for r in range(9):
    for c in range(9):
        v = board[r][c]
        if v == '.':
            continue
        box = (r // 3, c // 3)            # <- THE trick. not r//3 + c//3.
        if v in rows[r] or v in cols[c] or v in boxes[box]:
            return False
        rows[r].add(v); cols[c].add(v); boxes[box].add(v)
return True
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Sudoku Solver** (LC 37) | Backtracking with these same three sets as the pruning check — a direct sequel to your problem 22/39 work. |
| n×n board with √n boxes | Same code, replace 3 with `int(n ** 0.5)`. |
| Bitmask instead of sets | Nine bits per row/col/box. Faster and O(1) space, and a nice thing to offer as an optimisation. |
| Report ALL conflicts | Do not return early; collect them. |

## How to think about it next time

The general lesson is **normalisation**: rather than writing three different loops for three different geometries, find the coordinate transform that makes them identical. This turns up constantly — flattening a 2D index to 1D with `r*cols + c` (see LC 1260 in your repo), bucketing values with `v // bucket_size` (LC 164, LC 220), grouping by `(r//3, c//3)` here. When you find yourself writing near-duplicate code, look for the mapping that collapses it.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/valid-sudoku)
