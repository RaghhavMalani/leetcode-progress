# 2450. Minimum Replacements to Sort the Array
> **Hard** &nbsp;·&nbsp; Greedy from the right · equal splitting &nbsp;·&nbsp; family: **Greedy**

Two decisions carry the whole problem: process **right to left**, and when splitting, make the pieces as **equal** as possible so the leftmost one stays as large as it can.

**▶ [Step through this solution line by line](../visualizations/2450-minimum-replacements-to-sort-the-array.html)** — 8 steps, traced on `nums = [3,9,3]`.

| | |
|---|---|
| time | O(n) |
| space | O(n) recursion depth here; trivially O(1) as a loop |

## The idea

Two greedy choices, each with a one-line justification. **Direction:** the last element is unconstrained and can never benefit from splitting, so fix it and work leftwards — each element only has to fit under its right neighbour’s smallest piece. **Equal splitting:** given that you must break x into k parts, the leftmost part is what constrains everything further left, so maximise it — which means making the parts as equal as possible, giving ⌊x/k⌋.

## How to recognise it

- An operation that only **decreases** values, plus a sortedness requirement. Decrease-only almost always means "process from the unconstrained end".
- "Minimum number of operations" where each operation splits or reduces one element independently.
- Compare with LC 1846 in your repo: also decrease-only, but there you sort and climb from the left. The direction is decided by which end is free.

## Where people go wrong

- **Going left to right.** You have no idea what the right side needs yet, and no greedy choice is safe.
- **Splitting into pieces of size `bound` plus a remainder.** The remainder is small and drags the bound down; equal splitting is strictly better. This is the subtle error that makes an otherwise-correct solution wrong.
- **Ceiling division.** `(x + bound - 1) / bound` in C, or `-(-x // bound)` / `math.ceil` in Python. Getting it wrong by one changes k and the whole answer.
- **Recursion depth.** The C version recurses once per element; with n = 10⁵ that is fine in C but would need a loop in Python.

## The reusable template

```python
# process RIGHT to LEFT; the last element is unconstrained
bound = nums[-1]
ops = 0
for i in range(len(nums) - 2, -1, -1):
    x = nums[i]
    if x > bound:
        k = -(-x // bound)      # ceil(x / bound) = fewest pieces that fit
        ops += k - 1            # k pieces cost k-1 splits
        bound = x // k          # EQUAL split -> largest possible leftmost piece
    else:
        bound = x
return ops
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Non-increasing instead of non-decreasing | Mirror the direction — process left to right. |
| **Maximum Element After Decreasing and Rearranging** (LC 1846) | Decrease-only too, but rearrangement is allowed, so you sort and sweep left. Also in your repo. |
| Minimise the maximum piece instead of the operation count | Binary search on the answer. |
| Splitting has a per-piece cost | The greedy changes; you may need DP. |

## How to think about it next time

For "minimum operations to satisfy an ordering", ask two questions in order. **(1) Which end is unconstrained?** Start there — that element needs no work and anchors everything. **(2) Given a forced choice, which quantity constrains the rest, and how do I maximise it?** Here that quantity is the leftmost piece, and the answer is equal splitting. Those two questions produce the algorithm and its proof at the same time, which is exactly what you want to be able to say out loud.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/minimum-replacements-to-sort-the-array)
