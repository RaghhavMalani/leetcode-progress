# 1732. Find the Highest Altitude
> **Easy** &nbsp;&middot;&nbsp; Prefix sum · running maximum &nbsp;&middot;&nbsp; family: **Prefix sums & intervals**

A prefix sum with a running max, in four lines. The one thing to notice is that `max_altitude` must start at 0 — the starting point counts as a candidate.

**▶ [Step through this solution line by line](./visualization.html)** — 12 steps, traced on `gain = [-5,1,5,0,-7]`.

| | |
|---|---|
| time | O(n) |
| space | O(1) |

## The idea

When you are given **differences**, the positions are the prefix sums; when you are given positions, the differences are the deltas. Recognising which one you have been handed, and converting, is a tiny skill that unlocks a surprising number of problems.

## How to recognise it

- "gain", "change", "delta", "difference array" in the input description.
- Any question about the running total, or the max/min of the running total.
- The inverse trick — a **difference array** — turns "add x to every element in range [l,r]" into two O(1) updates plus one prefix pass at the end.

## Where people go wrong

- **Starting `max_altitude` at `gain[0]` or at −∞.** The biker starts at altitude 0, which may well be the highest point (all gains negative). Initialising to 0 is a correctness requirement, not a style choice.
- **Building the full altitude list.** Fine, but O(n) space for nothing.
- **Confusing gain[i] with altitude[i].** There are n gains and n+1 altitudes.

## The reusable template

```python
# differences -> positions is a prefix sum
alt = best = 0
for g in gain:
    alt += g
    best = max(best, alt)      # best starts at 0: the origin counts
return best

# the inverse: RANGE update, point query -> difference array
#   d[l] += x; d[r+1] -= x     then one prefix pass gives the final array
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Running Sum of 1d Array** (LC 1480) | Just emit the prefix sums. |
| **Maximum Subarray** (LC 53) | Kadane — running sum with a reset at 0. A cousin, not the same. |
| Range update, single query | **Difference array**: `d[l] += x; d[r+1] -= x`, prefix-sum once at the end. |
| **Range Sum Query** (LC 303 / 304) | Prefix sums answering many range queries. LC 304 is in your repo. |

## How to think about it next time

Add "prefix sum ↔ difference array" to your list of **reversible transforms**. Point updates + range queries → prefix sums. Range updates + point queries → difference array. Both → Fenwick tree (your LC 3739 uses one). Knowing which of those three you need takes five seconds and determines the whole solution.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/find-the-highest-altitude)
