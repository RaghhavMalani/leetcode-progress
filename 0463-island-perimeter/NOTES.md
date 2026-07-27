# 463. Island Perimeter
> **Easy** &nbsp;·&nbsp; Grid DFS · flood fill &nbsp;·&nbsp; family: **Graphs, BFS & DFS**

A flood fill where the return value counts the walls you bump into rather than the cells you visit. Watch the base cases: `return 1` means "I hit an edge", `return 0` means "already counted".

**▶ [Step through this solution line by line](../visualizations/0463-island-perimeter.html)** — 55 steps, traced on `grid = [[1,1],[1,0]]`.

| | |
|---|---|
| time | O(rows · cols) — each land cell is entered once |
| space | O(rows · cols) for the visit set and the recursion stack |

## The idea

Grid DFS is backtracking’s cousin: same recursion, but the "undo" is replaced by a **visited set that is never un-marked**. That single difference is what separates flood fill (visit each cell once, O(cells)) from path search (must un-mark so other paths can reuse the cell, exponential).

## How to recognise it

- A 2D grid, a notion of connected cells, and a question about a connected region: size, count, perimeter, shape.
- The four-way `directions` list and the "in bounds AND not visited AND is land" guard are the fingerprint.
- If the question is about **shortest** path or minimum steps, switch from DFS to BFS — DFS finds *a* path, BFS finds the shortest one.

## Where people go wrong

- **Marking visited after recursing instead of before.** Two adjacent land cells will call each other forever and blow the stack.
- **Bounds check after the array read.** `grid[i][j] == 0 or i < 0` crashes — Python’s negative indexing means `grid[-1]` silently wraps to the last row, which is worse than crashing because it gives a wrong answer quietly.
- **Recursion depth.** A 200 x 200 all-land grid is 40,000 deep and Python’s default limit is 1000. In an interview, say this out loud and offer the iterative stack version.
- **Assuming one island.** This problem guarantees it, hence the early `return` inside the double loop. LC 200 does not, and the same code would return after the first island only.

## The reusable template

```python
# Grid DFS / flood fill - the shape to memorise
DIRS = ((1,0), (-1,0), (0,1), (0,-1))

def dfs(r, c):
    if r < 0 or c < 0 or r >= ROWS or c >= COLS:   # bounds FIRST
        return 0
    if grid[r][c] != LAND or (r, c) in seen:       # then content
        return 0
    seen.add((r, c))                               # mark BEFORE recursing
    return 1 + sum(dfs(r+dr, c+dc) for dr, dc in DIRS)

# Counting PATHS instead of cells? Then you must un-mark:
#     seen.add((r,c)); total = ...recurse...; seen.remove((r,c))
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Number of Islands** (LC 200) | Do not return early — loop over every cell, and count how many times you start a fresh DFS. |
| **Max Area of Island** (LC 695) | Return `1 + sum(children)` instead of counting walls. |
| Shortest path across the grid | BFS with a queue, not DFS. Depth-first gives no shortness guarantee. |
| Perimeter without any search | Count land cells × 4, then subtract 2 for every adjacent land pair. O(cells), no recursion, and a strong answer to give first. |

## How to think about it next time

When you meet a grid problem, answer three questions before coding. **(1) DFS or BFS?** Shortest/level-by-level → BFS. Connectivity/whole-region → either, DFS is shorter. **(2) Do I un-mark?** Reachability → never un-mark. Counting distinct *paths* → you must un-mark on the way out. **(3) What does one call return?** Being able to finish the sentence "dfs(i,j) returns …" precisely is usually the entire difficulty; here it is "the number of perimeter edges reachable through this cell", which is why the water case returns 1.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/island-perimeter)
