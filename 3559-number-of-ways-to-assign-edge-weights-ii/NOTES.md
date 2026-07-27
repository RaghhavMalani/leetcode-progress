# 3559. Number of Ways to Assign Edge Weights II
> **Hard** &nbsp;·&nbsp; Binary lifting LCA + parity counting &nbsp;·&nbsp; family: **Trees**

Part I needed one tree height; Part II needs the distance between arbitrary pairs. That single change forces the whole LCA machinery — and the counting argument stays identical.

**▶ [Step through this solution line by line](../visualizations/3559-number-of-ways-to-assign-edge-weights-ii.html)** — 17 steps, traced on `a 5-node tree, then three queries`.

| | |
|---|---|
| time | O(n log n) preprocessing + O(log n) per query |
| space | O(n log n) |

## The idea

Three standard pieces. **(1) Distance formula:** dist(u,v) = depth[u] + depth[v] − 2·depth[LCA(u,v)] — the shared prefix is counted twice, so remove it twice. **(2) Binary lifting:** precompute 2^j-th ancestors so LCA is O(log n). **(3) Parity counting:** unchanged from Part I — half of the 2^d assignments satisfy the condition.

## How to recognise it

- **Many** path or ancestor queries on a static tree → binary lifting (or Euler tour + sparse table).
- Any tree distance question — the depth-minus-twice-LCA formula is universal.
- A "Part II" whose only change is "now there are queries" almost always means: precompute a structure that makes each query logarithmic.

## Where people go wrong

- **Recursive DFS.** With n = 10⁵ and a path-shaped tree it overflows. This solution uses an explicit stack for exactly that reason.
- **Lifting order.** Equalise depths FIRST, then lift both together. Doing it in the other order gives wrong ancestors.
- **The final step of LCA.** You lift while the ancestors DIFFER, which lands you on the LCA’s children — so the answer is `up[0][u]`, not `u`.
- **u == v.** Path length 0, and the answer must be 0, not 2^(−1).
- **Sizing LOG.** It must satisfy 2^LOG > n, or deep lifts silently truncate.
- **Recomputing powers of two per query.** Precompute the array once.

## The reusable template

```python
# tree distance = depth[u] + depth[v] - 2 * depth[LCA(u, v)]

LOG = n.bit_length()                 # must satisfy 2^LOG > n
up = [[0] * (n + 1) for _ in range(LOG)]

# iterative DFS (n can be 1e5 - do NOT recurse) fills depth[] and up[0][]
for j in range(1, LOG):              # up[j] = 2^j-th ancestor
    for v in range(1, n + 1):
        up[j][v] = up[j-1][ up[j-1][v] ]

def lca(u, v):
    if depth[u] < depth[v]: u, v = v, u
    diff = depth[u] - depth[v]
    for j in range(LOG):             # 1. equalise depths FIRST
        if diff >> j & 1: u = up[j][u]
    if u == v: return u
    for j in range(LOG - 1, -1, -1):  # 2. lift BOTH while they DIFFER
        if up[j][u] != up[j][v]:
            u, v = up[j][u], up[j][v]
    return up[0][u]                  # they stopped differing -> parent is the LCA
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Part I** (LC 3558) | One question about the height — a plain BFS. Also in your repo. |
| **LCA of a Binary Tree** (LC 236) | A single query, so a simple recursive search beats building any table. |
| Kth ancestor of a node | LC 1483 — the same table, queried directly. |
| Path sums instead of lengths | Store accumulated weights alongside the ancestor pointers. |
| Offline queries | Tarjan’s LCA with union-find — O(n α(n)) total, but only if you can batch. |

## How to think about it next time

The general move here is **trade preprocessing for query time**. One query? Do the simple linear thing. A million queries? Build a structure. Binary lifting, sparse tables, prefix sums and Fenwick trees are all instances of the same trade, and choosing between "just compute it" and "precompute a table" is mostly about reading the query count in the constraints. Notice too how little of Part II is new — the counting argument is identical, and all the added difficulty is infrastructure for answering many questions fast.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii)
