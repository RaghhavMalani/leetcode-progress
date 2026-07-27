# 1631. Path With Minimum Effort
> **Medium** &nbsp;·&nbsp; Dijkstra · minimax path &nbsp;·&nbsp; family: **Graphs, BFS & DFS**

Dijkstra where the path cost is the **maximum** edge rather than the sum. One character changes — `max` instead of `+` — and everything else about Dijkstra survives intact.

**▶ [Step through this solution line by line](../visualizations/1631-path-with-minimum-effort.html)** — 31 steps, traced on `heights = [[1,2,2],[3,8,2],[5,3,5]]`.

| | |
|---|---|
| time | O(mn log(mn)) |
| space | O(mn) |

## The idea

Dijkstra needs only that the cost function be **monotone non-decreasing along a path** — extending a path must never make it cheaper. Sum satisfies that for non-negative weights; so does max. So the "minimax path" (also called the bottleneck shortest path) is solvable by Dijkstra with the relaxation changed from `d + w` to `max(d, w)`.

## How to recognise it

- "Minimise the maximum" or "maximise the minimum" along a path — effort, bottleneck capacity, safest route.
- Weighted grid or graph plus a shortest-path flavour. Unweighted → BFS; non-negative sums → Dijkstra; may-be-negative → Bellman–Ford.
- Alternative framings: **binary search the answer** plus a BFS/DFS feasibility check, or a **union-find** that adds edges in increasing weight until the endpoints connect.

## Where people go wrong

- **Forgetting the stale-entry check.** Without `if (r,c) in visit: continue`, a cell gets processed multiple times and the complexity degrades. Since Python’s heapq has no decrease-key, this lazy-deletion guard is mandatory.
- **Marking visited on push instead of on pop.** That would freeze a cell at the first (possibly non-optimal) effort that reached it.
- **Using `+` out of habit.** Gives the wrong problem entirely.
- **Using BFS.** Edges are weighted, so BFS gives no optimality guarantee.

## The reusable template

```python
# Dijkstra with a MINIMAX cost - max(...) replaces (+)
heap = [(0, 0, 0)]                       # (cost so far, r, c)
visit = set()
while heap:
    d, r, c = heapq.heappop(heap)
    if (r, c) in visit:                  # STALE entry - lazy deletion.
        continue                         # mandatory: heapq has no decrease-key
    visit.add((r, c))                    # settle on POP, never on push
    if (r, c) == destination:
        return d
    for nr, nc in neighbours(r, c):
        if (nr, nc) in visit: continue
        nd = max(d, abs(h[r][c] - h[nr][nc]))     # <- SUM would be Dijkstra
        heapq.heappush(heap, (nd, nr, nc))

# also solvable by: binary search the answer + BFS check, or union-find
# adding edges in increasing weight until start and end connect.
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Swim in Rising Water** (LC 778) | Literally the same minimax Dijkstra with a different cost expression. |
| **Find the Safest Path in a Grid** (LC 2812) | MAXIMISE the minimum — a max-heap instead. Also in your repo. |
| **Network Delay Time** (LC 743) | Classic sum-based Dijkstra. |
| Binary search the answer | Guess a threshold k, then BFS using only steps ≤ k. O(mn log(maxHeight)) and often easier to explain. |
| Union-find | Sort edges by weight, union them in order, stop when start and end connect. Elegant and fast. |

## How to think about it next time

Do not memorise Dijkstra as "shortest sum of weights" — memorise it as "**settle the frontier in cost order, and the first time you settle a node its cost is final**". That framing makes it obvious the algorithm still works when the cost is a max, a product of probabilities, or anything else monotone. Then keep the three alternative attacks in mind — heap, binary-search-the-answer, union-find — because for bottleneck problems all three work and one of them is usually much easier to write correctly under pressure.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/path-with-minimum-effort)
