# 3532. Path Existence Queries in a Graph I
> **Medium** &nbsp;&middot;&nbsp; Sorted structure collapses a graph &nbsp;&middot;&nbsp; family: **Graphs, BFS & DFS**

Looks like a graph problem, is not one. Because `nums` is sorted, the graph is a chain that breaks at every gap larger than `maxDiff` — so components are just contiguous runs.

**▶ [Step through this solution line by line](./visualization.html)** — 16 steps, traced on `nums = [1,3,6,9], maxDiff = 2, then three queries`.

| | |
|---|---|
| time | O(n + q) |
| space | O(n) |

## The idea

Connectivity questions do not always need a connectivity algorithm. When nodes are laid out on a **sorted line** and edges only join nearby values, reachability becomes "are these two on the same unbroken run?" — answerable with one scan and one array lookup per query.

## How to recognise it

- A graph whose edges are defined by a **numeric closeness** condition on sorted data.
- Many queries against a static graph → precompute a component label, then O(1) per query. That is the same shape as union-find, but far cheaper here.
- If the array were NOT sorted, you would sort it (keeping original indices) and the same argument applies — that is exactly what Part II does.

## Where people go wrong

- **Building the adjacency list.** With n up to 10⁵ and dense closeness, the edge count can be O(n²) and you will run out of memory.
- **Running BFS or union-find per query.** O(q·n) instead of O(n + q).
- **Only comparing adjacent elements — and doubting it.** On sorted data, if i and i+1 are connected and i+1 and i+2 are connected, then i reaches i+2 *through* i+1 even if their direct gap is large. Transitivity is what makes the adjacent check sufficient.
- **Assuming the input is sorted when it is not.** Part I promises it; Part II does not.

## The reusable template

```python
# sorted + "edges join nearby values" -> components are contiguous runs
component = [0] * n
cid = 0
for i in range(1, n):
    if nums[i] - nums[i-1] > maxDiff:   # gap too big -> the chain snaps
        cid += 1
    component[i] = cid

# every query is then O(1)
return [component[u] == component[v] for u, v in queries]
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Part II** (LC 3534) | Same setup but the answer is the shortest path LENGTH. Sort, compute the farthest reachable index for each position, then binary lifting for O(log n) per query. Also in your repo. |
| Unsorted input | Sort with original indices, label components, map queries through the permutation. |
| Edges by absolute difference on 2D points | Sorting no longer works — union-find or a spatial index. |
| Dynamic edge insertions | Union-find with path compression is the right tool. |

## How to think about it next time

Before reaching for a graph algorithm, ask **"does the structure of the edges let me avoid building the graph?"** Edges defined by proximity on a line collapse to runs. Edges defined by a total order collapse to intervals. Edges defined by a hierarchy collapse to ancestor queries. Building the graph is often the expensive mistake — the intended solution frequently exploits the very structure that generated the edges.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/path-existence-queries-in-a-graph-i)
