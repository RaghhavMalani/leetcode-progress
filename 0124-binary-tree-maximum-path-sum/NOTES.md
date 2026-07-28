# 124. Binary Tree Maximum Path Sum
> **Hard** &nbsp;&middot;&nbsp; Tree DFS · return one thing, track another &nbsp;&middot;&nbsp; family: **Trees**

The problem that teaches the most important tree idea: **what a node returns to its parent is not the same as the answer it contributes.** Two quantities, computed at every node, and mixing them up is the entire failure mode.

**▶ [Step through this solution line by line](./visualization.html)** — 44 steps, traced on `root = [-10,9,20,null,null,15,7]`.

| | |
|---|---|
| time | O(n) — each node visited once |
| space | O(h) recursion depth |

## The idea

At each node compute two different things. **The contribution:** best path through this node using both children — that is a candidate for the global answer but cannot be extended upward, because a path through a node cannot also continue to its parent. **The return value:** best downward path starting here, using at most one child — that is what the parent can attach to. Keep them separate and the problem dissolves.

## How to recognise it

- A tree question whose answer might live **anywhere** in the tree, not necessarily at the root.
- The phrase "path" without "from root" — that is the tell that you need a global variable plus a different return value.
- The same shape solves LC 543 (diameter), LC 687 (longest univalue path), and LC 250. If you have seen one you have seen them all.

## Where people go wrong

- **Returning `node.val + left + right`.** The single most common bug. That path already forks at this node; the parent cannot extend it.
- **Not clamping negatives.** Without `max(x, 0)` a negative subtree drags the answer down instead of being skipped.
- **Initialising `res = 0`.** Fails when every value is negative — the answer is then the least-bad single node. `res = [root.val]` is correct.
- **Using a plain `res = ...` inside the nested function.** Python treats that as a new local. Use a list, or `nonlocal`.

## The reusable template

```python
# Tree DFS: return one thing, track another
res = [root.val]                       # or: nonlocal res

def dfs(node):
    if not node:
        return 0                       # a missing branch contributes 0
    l = max(dfs(node.left),  0)        # clamp: never take a harmful branch
    r = max(dfs(node.right), 0)

    res[0] = max(res[0], node.val + l + r)   # TRACK: path THROUGH this node
    return node.val + max(l, r)              # RETURN: one branch only

dfs(root)
return res[0]
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Diameter of a Binary Tree** (LC 543) | Identical structure with counts instead of sums: return `1 + max(l, r)`, track `l + r`. |
| Path must start at the root | No global needed — just return the max. |
| Path must go downward only (no turning) | Return and track become the same thing; much easier. |
| **Path Sum III** (LC 437) | Count paths summing to a target — prefix sums along the root-to-node path. |

## How to think about it next time

Whenever a tree DFS feels confusing, write out two sentences before coding: **"dfs(node) returns ___"** and **"the answer is updated using ___"**. If those two sentences are the same, the problem is easy. If they differ — as here — you need a global, and knowing that in advance is most of the solve. This "return one thing, track another" shape is the highest-yield idea in the entire tree category.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/binary-tree-maximum-path-sum)
