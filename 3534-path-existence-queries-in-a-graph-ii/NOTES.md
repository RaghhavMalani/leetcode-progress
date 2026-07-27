# 3534. Path Existence Queries in a Graph II
> **Hard** &nbsp;·&nbsp; Sort + greedy farthest + binary lifting &nbsp;·&nbsp; family: **Graphs, BFS & DFS**

Part I asked "are they connected?" and a component label answered it. Part II asks "how far apart?", and that needs a jump table — the same doubling trick used for lowest common ancestor.

**▶ [Step through this solution line by line](../visualizations/3534-path-existence-queries-in-a-graph-ii.html)** — 15 steps, traced on `nums = [1,8,3,10], maxDiff = 3, queries`.

| | |
|---|---|
| time | O(n log n) build + O(log n) per query |
| space | O(n log n) |

## The idea

Three layers. **(1) Sort** so that reachability becomes an interval property. **(2) Greedy farthest:** on a line, the fewest hops is always achieved by jumping as far right as possible each time — the same argument as Jump Game II. **(3) Binary lifting:** precompute 2^k-step jumps so that counting hops costs O(log n) instead of O(n) per query.

## How to recognise it

- Many queries asking for a **path length / ancestor / k-th successor** in a static structure. That combination is the binary-lifting signature.
- A deterministic "next" function (here `farthest`) that you must follow many times — precompute the doubling table.
- The greedy "always jump as far as possible" is valid whenever the reachable set from a position is a contiguous interval extending rightwards.

## Where people go wrong

- **Losing the original indices when sorting.** Queries refer to original nodes, so you need the `position[]` translation. This is the most common slip.
- **Forgetting the component check.** Without it the jump loop spins forever on unreachable pairs.
- **Off-by-one in the descent.** You jump while the destination stays *strictly before* the target, then add one final hop — hence `distance + 1` at the end of the real code.
- **Recomputing `farthest` with a nested loop.** The two-pointer sweep is O(n) because `right` is monotone; a naive inner loop is O(n²).
- **Sizing LOG wrongly.** It must satisfy 2^LOG > n, or long queries overflow the table.

## The reusable template

```python
# 1. sort, KEEPING original indices (queries refer to originals)
# 2. two pointers -> farthest[i] = rightmost index reachable in ONE hop
right = 0
for left in range(n):
    right = max(right, left)
    while right + 1 < n and values[right+1] - values[left] <= maxDiff:
        right += 1
    farthest[left] = right          # `right` is monotone -> the sweep is O(n)

# 3. binary lifting: jump[k][i] = 2^k hops from i
jump[0] = farthest
for k in range(1, LOG):             # LOG must satisfy 2^LOG > n
    for i in range(n):
        jump[k][i] = jump[k-1][jump[k-1][i]]

# query: take the LARGEST jumps that do not overshoot, then one final hop
cur, dist = left, 0
for k in range(LOG - 1, -1, -1):
    if jump[k][cur] < right:
        cur = jump[k][cur]; dist += 1 << k
return dist + 1
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Part I** (42 3532) | Only connectivity, so a component label is enough. Also in your repo. |
| **Jump Game II** (42 45) | The same greedy-farthest argument, single query, O(n). |
| 42A in a tree | Binary lifting on parent pointers — the canonical use. |
| k-th successor in a functional graph | 42 2836 — exactly this jump table. |
| Weighted hops | Store the accumulated weight alongside the jump target. |

## How to think about it next time

**Binary lifting is the answer to "follow this pointer many times, many times over."** Whenever you have a static successor function and repeated queries about following it, precompute jumps of 2⁰, 2¹, 2², … and answer each query by decomposing the count into binary. It powers 42A, k-th ancestor, k-th successor, and range-minimum sparse tables. Learning it once pays off across a whole tier of Hard problems — and the tell is always "static structure + many path queries".

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/path-existence-queries-in-a-graph-ii)
