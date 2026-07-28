# 62. Unique Paths
> **Medium** &nbsp;&middot;&nbsp; Grid DP · rolling row &nbsp;&middot;&nbsp; family: **Dynamic programming**

Grid DP solved bottom-up, keeping only one row. Same recurrence as the m×n table version, one dimension of memory less — and there is also a pure combinatorics answer with no DP at all.

**▶ [Step through this solution line by line](./visualization.html)** — 18 steps, traced on `m = 3, n = 7`.

| | |
|---|---|
| time | O(m·n) |
| space | O(n) — one row; the naive table is O(m·n) |

## The idea

paths(r, c) = paths(r+1, c) + paths(r, c+1), because the first move is either down or right and those two sets of paths are disjoint. Because each row only depends on the row directly below it, you can throw away everything else — the classic **rolling array** optimisation for grid DP.

## How to recognise it

- Movement on a grid restricted to two directions (right/down), counting paths or minimising cost.
- A recurrence where cell (r,c) depends only on (r±1, c) and (r, c±1) — that locality is what permits the rolling row.
- Whenever the DP table row i depends only on row i−1, the space drops by a whole dimension.

## Where people go wrong

- **Iterating in the wrong direction.** This code fills newRow from right to left because `newRow[j]` needs `newRow[j+1]`, which must already be final. Reverse it and you read a stale value.
- **Boundaries.** The last row and last column are all 1s. Initialising with `[1] * n` handles both without an `if`.
- **Confusing m and n.** m is rows, n is columns. Swapping them still gives the right answer here (the formula is symmetric) but will bite you the moment obstacles are added.
- **Missing the combinatorics.** The answer is C(m+n−2, m−1) — you make m+n−2 moves and choose which m−1 are "down". O(min(m,n)) with no DP at all, and interviewers love that you noticed.

## The reusable template

```python
# Grid DP with a rolling row - O(n) space instead of O(m*n)
row = [1] * n                      # the bottom row: one path from anywhere
for _ in range(m - 1):
    newRow = [1] * n               # last column is 1 -> no boundary branch
    for j in range(n - 2, -1, -1): # RIGHT to LEFT: newRow[j+1] must be final
        newRow[j] = newRow[j + 1] + row[j]     # right + below
    row = newRow
return row[0]

# and the closed form, worth stating:  C(m + n - 2, m - 1)
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Unique Paths II** (LC 63) | Obstacles — set blocked cells to 0. The combinatorics shortcut dies here, which is the point of the sequel. |
| **Minimum Path Sum** (LC 64) | Replace `+` with `min` and add the cell cost. |
| Diagonal moves allowed | Three terms in the recurrence instead of two. |
| Combinatorial answer | C(m+n−2, m−1). Give this alongside the DP. |
| **Number of Paths with Max Score** (LC 1301) | Two DP tables in parallel — best score and how many ways achieve it. |

## How to think about it next time

Two habits from this problem. First: **always check whether a counting DP has a closed form.** Paths on an unobstructed grid, balanced parentheses, binary strings with no two adjacent 1s — all have formulas, and spotting one is free credit. Second: **after writing any 2D DP, ask which rows the recurrence actually reaches back to.** If it is only the previous one, you can drop to a single array; if only the previous cell, to a single variable. That reduction is asked for so often it should be automatic.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/unique-paths)
