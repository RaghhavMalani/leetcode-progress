# 1288. Remove Covered Intervals
> **Medium** &nbsp;&middot;&nbsp; Intervals · sort key does the work &nbsp;&middot;&nbsp; family: **Prefix sums & intervals**

A five-line loop that is only correct because of one sort key. `(x[0], -x[1])` — start ascending, **end descending** — is the entire algorithm; everything after it is a running maximum.

**▶ [Step through this solution line by line](./visualization.html)** — 9 steps, traced on `intervals = [[1,4],[3,6],[2,8]]`.

| | |
|---|---|
| time | O(n log n) — dominated by the sort |
| space | O(1) beyond the sort |

## The idea

Choosing a sort order that makes one dimension monotone lets you replace pairwise comparison with a **running maximum** over the other dimension. Here start becomes non-decreasing, so "am I covered?" reduces entirely to "is my end ≤ the biggest end so far?".

## How to recognise it

- Containment / dominance between 2D items — intervals, (width, height) pairs, (score, rank).
- The naive answer is an O(n²) all-pairs check; a sort collapses one dimension and a sweep handles the other.
- Same idea powers Russian doll envelopes (LC 354), where after sorting by width the problem becomes a longest increasing subsequence on height.

## Where people go wrong

- **Sorting by (start asc, end asc).** The killer bug. With [1,4] and [1,6] in that order, [1,6] is compared against max_end = 4, looks longer, gets kept — but [1,4] was already wrongly counted as a survivor. Descending end puts the container first.
- **Using `>=` instead of `>`.** An interval with exactly the same end as a previous one IS covered.
- **Initialising `max_end` badly.** 0 works because the constraints say values are positive; use −∞ if they might not be.
- **Trying to do it without sorting.** There is no O(n) solution; the sort is the algorithm.

## The reusable template

```python
# The sort key IS the algorithm
intervals.sort(key=lambda x: (x[0], -x[1]))   # start ASC, end DESC

count, max_end = 0, 0
for start, end in intervals:
    if end > max_end:          # reaches further right than anything before
        count += 1             # -> cannot be covered
        max_end = end
return count

# with (start, +end) the equal-start case breaks: the CONTAINED interval
# would come first and be counted as a survivor.
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Merge Intervals** (LC 56) | Sort by start, merge overlapping neighbours. |
| **Non-overlapping Intervals** (LC 435) | Sort by END, greedily keep the earliest finisher. |
| **Russian Doll Envelopes** (LC 354) | Sort by (width asc, height desc) — exactly this tie-break — then LIS on heights. |
| Count how many intervals cover each point | A sweep line with +1/−1 events. |

## How to think about it next time

When a problem involves two dimensions and a "dominates / contains / fits inside" relation, the reflex should be: **sort by one dimension to make it monotone, then the other dimension becomes a running max/min or an LIS.** And pay very close attention to the tie-break — in this family the tie-break is not a detail, it is the correctness argument. If you cannot say in one sentence why your tie-break direction is right, you have a bug waiting.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/remove-covered-intervals)
