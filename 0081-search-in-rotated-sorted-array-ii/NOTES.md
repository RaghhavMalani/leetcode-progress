# 81. Search in Rotated Sorted Array II
> **Medium** &nbsp;&middot;&nbsp; Binary search · rotated + duplicates &nbsp;&middot;&nbsp; family: **Binary search**

Binary search when the array is rotated AND has duplicates. The duplicate case is the interesting one: when `nums[left] == nums[mid]` you genuinely cannot tell which half is sorted, and the algorithm degrades to O(n).

**▶ [Step through this solution line by line](./visualization.html)** — 4 steps, traced on `nums = [2,5,6,0,0,1,2], target = 0`.

| | |
|---|---|
| time | O(log n) average, **O(n) worst case** — e.g. [1,1,1,1,1,0,1] |
| space | O(1) |

## The idea

You can still halve the search space without knowing where the rotation is, because **at least one half of any split is sorted**. Identify which one, test the target against its known range, and discard accordingly. Duplicates break the identification, and the honest response is to give up one element and retry.

## How to recognise it

- "Rotated sorted array" — with or without duplicates. Check which, because it changes the achievable complexity.
- More generally: a structure that is *locally* sorted in pieces. Find the piece you can reason about, use it, discard the rest.
- If duplicates are allowed and someone claims O(log n), they are wrong — and being able to give the counterexample [1,1,1,0,1] is worth real credit.

## Where people go wrong

- **Forgetting the duplicate branch entirely.** Your LC 33 solution ported straight over will infinite-loop or give wrong answers on [1,0,1,1,1].
- **Comparing against `nums[mid]` and `nums[right]` inconsistently.** Pick one anchor — `nums[left]` here — and use it in every branch.
- **Inclusive vs exclusive range boundaries in the target test.** `nums[left] <= target < nums[mid]`: left inclusive because it could BE the answer, mid exclusive because we already tested it. Get these backwards and you drop valid answers.
- **Claiming O(log n).** Say the worst case out loud; that is the point of this problem existing separately from LC 33.

## The reusable template

```python
# Rotated sorted array - identify the sorted half, then decide
while lo <= hi:
    mid = (lo + hi) // 2
    if a[mid] == target: return True

    if a[lo] == a[mid]:          # DUPLICATES: cannot tell. give up one element.
        lo += 1; continue        # (omit this branch for LC 33 - no duplicates)

    if a[lo] < a[mid]:           # left half [lo..mid] is sorted
        if a[lo] <= target < a[mid]: hi = mid - 1
        else:                        lo = mid + 1
    else:                        # right half [mid..hi] is sorted
        if a[mid] < target <= a[hi]: lo = mid + 1
        else:                        hi = mid - 1
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| No duplicates | LC 33 — drop the `nums[left] == nums[mid]` branch, and it is genuinely O(log n). |
| **Find the minimum** in a rotated array | LC 153 / 154 — compare against `nums[right]`, no target involved. |
| Find the rotation index | Same as finding the minimum. |
| Rotated but you may sort first | O(n log n) and you have thrown the problem away — but state it as the baseline. |

## How to think about it next time

The reusable idea: **when a structure is not globally ordered, look for a piece that is.** Rotated array → one sorted half. Mountain array → one monotone side. 2D sorted matrix → start at a corner where the comparison is unambiguous. In every case the question is "where do I stand so that a single comparison eliminates a large chunk?" Answer that and the code follows.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array-ii)
