# 3558. Number of Ways to Assign Edge Weights I
> **Medium** &nbsp;·&nbsp; BFS height + parity counting &nbsp;·&nbsp; family: **Graphs, BFS & DFS**

BFS to measure the tree height, then a counting argument: exactly half of all 2^d weight assignments satisfy any fixed parity condition, so the answer is 2^(d−1).

**▶ [Step through this solution line by line](../visualizations/3558-number-of-ways-to-assign-edge-weights-i.html)** — 11 steps, traced on `edges = [[1,2],[1,3],[3,4],[3,5]]`.

| | |
|---|---|
| time | O(n) for the BFS + O(log d) for the power |
| space | O(n) |

## The idea

Two independent pieces. **Level-order BFS** with the `for _ in range(len(queue))` idiom measures the height cleanly. **Parity counting:** when each of d independent binary choices flips a parity bit, exactly half of the 2^d outcomes land on each parity — so any single parity constraint halves the count, giving 2^(d−1).

## How to recognise it

- Level-by-level tree processing: height, level sums, zigzag order, right-side view. The drain-one-level loop is the universal shape.
- "Count assignments satisfying a parity / mod-2 condition" — the answer is almost always half of the total, which is why these problems have one-line answers.
- Large exponents with a modulus → `pow(base, exp, MOD)`, never a loop.

## Where people go wrong

- **Off-by-one between levels and edges.** A tree with L levels has a longest path of L−1 edges. Hence `d = depth - 1`, and then the exponent is d−1 again. Check on a two-node tree.
- **Forgetting `visited` in an undirected tree.** The adjacency list contains both directions, so without it BFS walks back to the parent forever.
- **Not draining exactly one level per iteration.** Capture `len(queue)` BEFORE the inner loop — the queue grows while you drain it.
- **Computing 2^d then dividing.** Under a modulus you cannot divide directly; compute 2^(d−1) instead, or multiply by the modular inverse.
- **d = 0 (a single node).** Then 2^(−1) is meaningless — worth guarding if the constraints allow it.

## The reusable template

```python
# level-order BFS: capture the level size BEFORE draining
q, seen, depth = deque([root]), {root}, 0
while q:
    depth += 1
    for _ in range(len(q)):        # len() captured now; the queue grows below
        node = q.popleft()
        for nxt in adj[node]:
            if nxt not in seen:
                seen.add(nxt); q.append(nxt)

d = depth - 1                       # LEVELS - 1 = edges on the longest path
return pow(2, d - 1, MOD)           # half of 2^d satisfy any fixed parity
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Part II** (LC 3559) | Queries between arbitrary node pairs, so you need LCA (binary lifting) to get each path length. Also in your repo. |
| **Binary Tree Level Order Traversal** (LC 102) | The same drain-one-level loop, collecting values. |
| Count assignments with a SUM condition | Parity no longer suffices — generating functions or DP. |
| Weighted edges from a larger set | The count per edge changes from 2 to k; the parity argument may not survive. |

## How to think about it next time

When a counting problem involves independent binary choices and a mod-2 condition, reach for the **halving argument** before writing any DP: flipping any single choice flips the parity, which pairs the outcomes up perfectly, so exactly half satisfy the condition. That one observation collapses a whole family of problems to a single power. And keep the level-order BFS idiom in your fingers — capture the level size first, then drain it — because it is the backbone of a dozen tree problems.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i)
