# 128. Longest Consecutive Sequence
> **Medium** &nbsp;·&nbsp; Hash set · amortised scan &nbsp;·&nbsp; family: **Hashing**

A nested loop that is nevertheless O(n). The guard `if (num-1) not in s` is what makes it so: each run is walked from its start exactly once, so the inner loop does n total work across the whole run of the outer loop.

**▶ [Step through this solution line by line](../visualizations/0128-longest-consecutive-sequence.html)** — 26 steps, traced on `nums = [100,4,200,1,3,2]`.

| | |
|---|---|
| time | O(n) — amortised; each value is the inner-loop subject at most once |
| space | O(n) for the set |

## The idea

**Amortised analysis**: a loop nested inside a loop is not automatically O(n²). What matters is the total number of inner iterations across the entire run. Here the guard ensures each value is stepped over by exactly one inner walk, so the inner loop contributes n steps in total, not n per outer iteration.

## How to recognise it

- "Consecutive", "sequence of adjacent values", "gap of exactly 1" — and an explicit O(n) requirement that rules out sorting.
- Order in the input does not matter, only membership. That is the signal to build a set and stop thinking about positions.
- If sorting were allowed, the O(n log n) sort-and-scan is far easier to write; say that first, then give this.

## Where people go wrong

- **Dropping the `num-1` guard.** Without it you re-walk each run from every one of its members and the solution really is O(n²).
- **Iterating over `nums` instead of `s`.** Correct, but duplicates make you redo work. Iterating the set is free deduplication.
- **Off-by-one in the walk.** `while (length + num) in s` starts with length 0, so it first tests `num` itself — that is why the final length is the count, not the count minus one.
- **Forgetting the empty input.** `longest = 0` handles it; initialising to 1 does not.

## The reusable template

```python
# Amortised scan - only start work where work has not been done
s = set(nums)
best = 0
for x in s:
    if x - 1 in s:        # not the start of a run -> someone else handles it
        continue
    n = 0
    while x + n in s:     # walk the run exactly once, ever
        n += 1
    best = max(best, n)
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Return the sequence itself, not its length | Track the start value alongside the max length. |
| Consecutive with gaps of at most g | The set trick breaks down — sort and scan instead. |
| Streaming input | Union-find, merging a new value with its neighbours as it arrives. |
| **Binary Tree Longest Consecutive** (LC 298) | Same word, completely different machinery — DFS carrying the current run length. |

## How to think about it next time

When you see a nested loop and instinctively think "that is O(n²)", stop and ask **how many times can the inner loop body run across the entire execution?** If each element can only be the subject of the inner loop once, the answer is n and you have a linear algorithm. This same reasoning is what makes the sliding window O(n), and what makes the monotonic stack in LC 739 O(n). It is one idea in three costumes.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/longest-consecutive-sequence)
