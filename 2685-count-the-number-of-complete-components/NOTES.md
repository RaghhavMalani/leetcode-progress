# 2685. Count the Number of Complete Components
> **Medium** &nbsp;&middot;&nbsp; Connected components + a counting criterion &nbsp;&middot;&nbsp; family: **Graphs, BFS & DFS**

Two standard pieces: DFS to find components, and the handshake lemma to test completeness by counting edges instead of checking every pair.

**▶ [Step through this solution line by line](./visualization.html)** — 21 steps, traced on `n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]`.

| | |
|---|---|
| time | O(n + e) |
| space | O(n + e) |

## The idea

Two ideas. **Component discovery:** loop over all nodes, and every unvisited one starts a DFS/BFS that consumes its whole component — the standard O(n + e) sweep. **Handshake lemma:** the sum of degrees equals twice the edge count, so you can get a component’s edge count without touching the edge list, and compare it against C(v, 2).

## How to recognise it

- Any per-component property: size, edge count, is-it-a-tree, is-it-bipartite, is-it-complete.
- "Complete graph" = every pair joined = exactly v(v−1)/2 edges. Similarly "is a tree" = connected and exactly v−1 edges.
- Union-find is the natural alternative and is often shorter: union everything, then group by root and count edges per root.

## Where people go wrong

- **Forgetting to divide the degree sum by 2.** The handshake lemma is the whole point of the criterion.
- **Checking every pair for an edge.** O(v²) per component and unnecessary.
- **Recursion depth.** With n up to 5×10⁴ and a path-shaped graph, recursive DFS blows the stack in Python — use an explicit stack or BFS.
- **Not resetting the per-component accumulators.** They must be zeroed for each new DFS.
- **Self-loops or duplicate edges.** They break the degree arithmetic; the constraints here forbid them, and it is worth saying so.

## The reusable template

```python
# sweep + DFS per component, accumulate, then apply a criterion
def count_components(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v); adj[v].append(u)

    seen, ans = [False] * n, 0
    for start in range(n):
        if seen[start]:
            continue
        verts = deg_sum = 0
        stack = [start]; seen[start] = True        # ITERATIVE: no depth limit
        while stack:
            u = stack.pop()
            verts += 1; deg_sum += len(adj[u])
            for w in adj[u]:
                if not seen[w]:
                    seen[w] = True; stack.append(w)

        edges_in = deg_sum // 2                    # handshake lemma
        if edges_in == verts * (verts - 1) // 2:   # complete?  (tree: verts - 1)
            ans += 1
    return ans
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Union-find version | Union all edges, then count vertices and edges per root. Often shorter and iterative by nature. |
| Count components that are TREES | Same sweep, criterion becomes `edges == vertices - 1`. |
| **Number of Provinces** (LC 547) | Just count the components; no criterion. |
| Bipartite check per component | DFS with 2-colouring instead of counting. |

## How to think about it next time

Separate **traversal** from **criterion**. The sweep-and-DFS that enumerates components is boilerplate you should be able to write without thinking; what changes between problems is only the quantity you accumulate and the test you apply at the end. Write the boilerplate first, leave a hole for "what do I measure?", and then think hard only about the criterion — here, edges vs C(v,2), which the handshake lemma makes free.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/count-the-number-of-complete-components)
