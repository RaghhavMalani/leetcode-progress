# 2812. Find the Safest Path in a Grid
> **Medium** &nbsp;·&nbsp; Multi-source BFS + maximin Dijkstra &nbsp;·&nbsp; family: **Graphs, BFS & DFS**

Two classic techniques stacked. Multi-source BFS builds a distance field from all thieves at once; then a max-heap search finds the path whose weakest cell is as strong as possible.

**▶ [Step through this solution line by line](../visualizations/2812-find-the-safest-path-in-a-grid.html)** — 36 steps, traced on `grid = [[0,0,1],[0,0,0],[0,0,0]]`.

| | |
|---|---|
| time | O(n² log n) — BFS is O(n²), the heap search dominates |
| space | O(n²) |

## The idea

**Multi-source BFS**: to find every cell’s distance to the *nearest* of many sources, seed the queue with all of them at distance 0 and run one BFS. It costs the same as a single-source BFS. **Maximin path**: a path’s value is its weakest link, so relax with `min(current, cell)` and pop the largest first.

## How to recognise it

- Multi-source BFS: "distance to the nearest X" for many X — rotting oranges, walls and gates, nearest 0.
- Maximin/minimax path: "maximise the minimum" or "minimise the maximum" along a route.
- Two-phase structure: whenever a problem needs a derived quantity per cell before the real search, compute the whole field first.

## Where people go wrong

- **Running BFS once per source.** O(sources × n²) instead of O(n²). Seeding them all together is the whole point.
- **Negating for the max-heap and forgetting to negate back.** Line 32 (`safe = -safe`) is easy to drop and the bug is silent.
- **Using `+` or `max` in the relaxation.** A path is as safe as its worst cell, so it must be `min`.
- **Marking visited on push here** — which is correct in this variant because the max-heap pops in decreasing order, but be aware it differs from the lazy-deletion style used in LC 1631.
- **Forgetting the start and end cells count** towards the safeness.

## The reusable template

```python
# 1. multi-source BFS: seed EVERY source at distance 0, run ONE bfs
q = deque((r, c) for r, c in all_sources)
for r, c in all_sources: dist[r][c] = 0
while q:
    r, c = q.popleft()
    for nr, nc in nbrs(r, c):
        if dist[nr][nc] == -1:          # -1 doubles as "unvisited"
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))

# 2. maximin path: max-heap (negate for heapq), relax with min()
heap = [(-dist[0][0], 0, 0)]
while heap:
    safe, r, c = heapq.heappop(heap); safe = -safe      # NEGATE BACK
    if (r, c) == goal: return safe
    for nr, nc in nbrs(r, c):
        if not seen[nr][nc]:
            seen[nr][nc] = True
            heapq.heappush(heap, (-min(safe, dist[nr][nc]), nr, nc))
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Rotting Oranges** (LC 994) | Multi-source BFS, and the answer is the final level count. |
| **Walls and Gates** (LC 286) | Multi-source BFS from every gate. |
| **01 Matrix** (LC 542) | Multi-source BFS from every zero. |
| **Path With Minimum Effort** (LC 1631) | The mirror image — minimise the maximum with a min-heap. Also in your repo. |
| Binary search the answer | Guess a safeness s, then BFS through cells with dist ≥ s. Often easier to write than the heap version. |

## How to think about it next time

Two habits. First: when many sources need a "distance to nearest" field, **think super-source** — one BFS, all seeds. The same idea works for multi-source Dijkstra and for topological sort with many roots. Second: recognise the maximin/minimax family and remember it always admits **three** solutions — heap, binary-search-the-answer, or union-find. Under time pressure, binary search plus a simple reachability check is usually the one you can get right first try.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/find-the-safest-path-in-a-grid)
