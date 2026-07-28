# 57. Insert Interval
> **Medium** &nbsp;&middot;&nbsp; Intervals · three-case scan &nbsp;&middot;&nbsp; family: **Prefix sums & intervals**

Three mutually exclusive cases — after, before, overlapping — and the elegant bit is case 3: the new interval keeps *absorbing* neighbours rather than being appended immediately.

**▶ [Step through this solution line by line](./visualization.html)** — 6 steps, traced on `intervals = [[1,3],[6,9]], newInterval = [2,5]`.

| | |
|---|---|
| time | O(n) — no sort needed |
| space | O(n) for the output |

## The idea

Two intervals [a,b] and [c,d] **overlap iff a ≤ d and c ≤ b**. Everything else is the negation of that, which is where the two clean early cases come from. When they do overlap, the union is `[min(a,c), max(b,d)]` — and you keep merging into the same accumulator because one new interval can swallow an arbitrarily long run.

## How to recognise it

- Interval / range / meeting-room problems. Almost all of them start with "sort by start", and this one is handed that for free.
- The three-way split (disjoint left, disjoint right, overlapping) is the standard case analysis; write those three branches before you write any code.
- If the input were NOT sorted, you would sort first and the problem becomes LC 56.

## Where people go wrong

- **Appending newInterval as soon as you see an overlap.** It may absorb several more; only append once the overlap run is over.
- **Strict vs non-strict comparisons.** Do [1,3] and [3,5] touch? This code uses `<` so they merge. LeetCode wants them merged; a real scheduling problem often does not. Check the definition.
- **Forgetting the append after the loop.** If newInterval extends past the last interval, case 1 never fires and it would be silently dropped.
- **Sorting unnecessarily.** The input is already sorted; adding a sort is O(n log n) for nothing and signals you did not read the constraints.

## The reusable template

```python
# Intervals: three cases, one pass (input already sorted)
res = []
for i, (s, e) in enumerate(intervals):
    if new[1] < s:                      # entirely AFTER new -> done
        return res + [new] + intervals[i:]
    elif new[0] > e:                    # entirely BEFORE new -> copy across
        res.append([s, e])
    else:                               # OVERLAP -> absorb, do not append yet
        new = [min(new[0], s), max(new[1], e)]
res.append(new)                         # never got placed -> it goes last
return res

# overlap test:  a <= d and c <= b        union: [min(a,c), max(b,d)]
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Merge Intervals** (LC 56) | Sort by start, then sweep merging into the last result element. |
| **Non-overlapping Intervals** (LC 435) | Sort by END and greedily keep the earliest finisher — a different sort key entirely. |
| **Meeting Rooms II** (LC 253) | A min-heap of end times, or a +1/−1 sweep line over the boundaries. |
| **Remove Covered Intervals** (LC 1288) | Sort by (start asc, end desc). Also in your repo — see how the sort key does all the work there. |

## How to think about it next time

Interval problems are decided almost entirely by **the sort key**. Sort by start → merging and insertion. Sort by end → greedy "keep as many as possible" (activity selection). Sort by (start, −end) → covering relationships. Before writing anything, ask "what order makes the greedy choice locally obvious?" Getting that right turns most interval problems into a five-line sweep; getting it wrong makes them impossible.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/insert-interval)
