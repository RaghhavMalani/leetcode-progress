# 40. Combination Sum II
> **Medium** &nbsp;·&nbsp; Backtracking · duplicate suppression &nbsp;·&nbsp; family: **Backtracking**

One while loop is the entire problem. Watch the step where `i` jumps from 0 to 1 — that is the line separating a correct answer from one with duplicate rows.

**▶ [Step through this solution line by line](../visualizations/0040-combination-sum-ii.html)** — 37 steps, traced on `candidates = [1,1,2], target = 3`.

| | |
|---|---|
| time | O(2ⁿ · n) — every subset may be visited, n to copy each hit |
| space | O(n) depth |

## The idea

Two things are happening and they are easy to confuse. **Single use** is handled by recursing on `i+1`. **Duplicate answers** are handled by the while loop. They are independent bugs with independent fixes: get one right and you can still fail the other.

## How to recognise it

- The input **contains repeated values** and the output must have **no repeated rows**. That combination is the signature.
- Each element usable at most once → recurse on `i+1`.
- If the input were guaranteed distinct, the while loop would be dead code — this is worth saying out loud in an interview.

## Where people go wrong

- **Forgetting `sort()`.** The while loop compares *neighbours*. Unsorted, equal values are scattered and the skip never triggers.
- **Deduping with a set of tuples at the end.** It works and it is the answer people reach for under pressure, but it does the exponential work anyway and then throws it away. The interviewer is watching for the in-tree fix.
- **Putting the skip on the take branch.** Skipping duplicates when you *take* is wrong — [1,1] is a legitimate answer. You only skip on the branch that *excludes* the value.
- **Off-by-one in the while condition.** `i+1 < len` guards the read of `candidates[i+1]`; drop it and you index out of range on the last element.

## The reusable template

```python
# Killing duplicates - two interchangeable idioms.

# (a) sort + skip equal neighbours   (LC 40, 90)
arr.sort()
subset.append(arr[i]); backtrack(i+1); subset.pop()
while i+1 < len(arr) and arr[i] == arr[i+1]:
    i += 1
backtrack(i+1)                # the "skip" branch lands on a NEW value

# (b) loop over distinct values with a count budget   (LC 47)
for val in count:             # keys, not positions
    if count[val] > 0:
        path.append(val); count[val] -= 1
        backtrack()
        count[val] += 1; path.pop()
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Input distinct, unlimited reuse | LC 39 — drop the while loop, recurse on `i` not `i+1`. |
| **Subsets II** (LC 90) | Identical machinery, no target: every node is an answer instead of only the ones that hit the sum. |
| **Permutations II** (LC 47) | Same goal, different weapon — count distinct values rather than skip duplicate positions. |
| Duplicates allowed in output | Delete the while loop. Nothing else changes. |

## How to think about it next time

When an input has duplicates, ask: **what makes two branches produce the same answer?** Here it is that positions 0 and 1 hold the same value, so "skip position 0, take position 1" produces exactly what "take position 0" already produced. The fix is always the same shape — *at each level, consider each distinct value at most once*. Sorting is what makes "distinct value" cheap to detect. Carry that sentence into 47 and 90 and you will not have to re-derive anything.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/combination-sum-ii)
