# 3620. Network Recovery Pathways
> **Hard** &nbsp;&middot;&nbsp; Binary search on the answer + DAG shortest path &nbsp;&middot;&nbsp; family: **Binary search**

The most transferable technique in competitive programming: when the answer is hard to compute but easy to *verify*, binary search it. Here each verification is a linear sweep over a topological order.

**▶ [Step through this solution line by line](./visualization.html)** — 16 steps, traced on `n = 4, edges = [[0,1,5],[1,3,10],[0,2,4],[2,3,4]], k = 10`.

| | |
|---|---|
| time | O((V + E) · log maxCost) |
| space | O(V + E) |

## The idea

**Binary search on the answer.** Instead of computing the optimum directly, guess a value x and ask a yes/no question: "is x achievable?" If `can(x)` is monotone — true for all x below the optimum and false above — binary search finds the boundary in O(log range) checks. The hard work moves into writing `can()`, which is usually a much simpler problem.

## How to recognise it

- "Maximise the minimum" or "minimise the maximum" — the phrase is almost a guarantee.
- The answer lies in a known numeric range and checking a candidate is easier than optimising directly.
- On a **DAG**, shortest paths need no Dijkstra: relax edges in topological order and one linear sweep suffices — and it even works with negative weights.
- Companions in your repo: LC 1631 (minimise the maximum) and LC 2812 (maximise the minimum), both solvable this way as well as with a heap.

## Where people go wrong

- **Not verifying monotonicity.** If `can()` is not monotone, binary search returns nonsense. State the argument: raising the threshold only removes edges, so feasibility can only get worse.
- **Recomputing the topological order inside `can()`.** The DAG never changes — compute it once outside the loop.
- **The `ans = mid; left = mid + 1` pattern.** Because we want the LARGEST feasible value, record on success and keep pushing upward. Getting this direction backwards is the classic binary-search-on-answer bug.
- **Initialising `ans = -1`.** Necessary — nothing may be feasible at all.
- **Forgetting the offline-node and budget prunes** inside the relaxation; they are part of the feasibility definition, not optimisations.

## The reusable template

```python
# binary search on the ANSWER - the search is always the same 10 lines
lo, hi, ans = 0, MAX_POSSIBLE, -1
while lo <= hi:
    mid = (lo + hi) // 2
    if can(mid):
        ans = mid          # feasible -> record it and try HIGHER
        lo  = mid + 1      # (minimising instead? record and go LOWER)
    else:
        hi  = mid - 1
return ans

# can() on a DAG: one linear sweep in topological order, no heap needed
#   for u in topo:
#       for v, w in graph[u]:
#           dist[v] = min(dist[v], dist[u] + w)
# monotonicity check: raising the threshold only REMOVES options -> monotone.
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Koko Eating Bananas** (LC 875) | Binary search the eating speed; `can()` is a sum of ceilings. |
| **Split Array Largest Sum** (LC 410) | Binary search the largest allowed subarray sum; `can()` is a greedy split. |
| **Path With Minimum Effort** (LC 1631) | Binary search the effort; `can()` is a BFS. Also in your repo. |
| **Capacity to Ship Packages** (LC 1011) | Same shape with weights and days. |
| Graph has cycles | Topological order does not exist — use Dijkstra inside `can()` instead. |

## How to think about it next time

Whenever a problem asks for an optimum and you cannot see how to compute it, **flip it into a decision problem**: "given a candidate x, can I achieve it?" If that question is easier and its answer is monotone in x, you are done — binary search does the rest. This one reframing turns a large family of Hard problems into Medium ones, and the tell is almost always the phrase "maximise the minimum" or "minimise the maximum". Practise writing `can()` first and the search second; the search is always the same ten lines.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/network-recovery-pathways)
