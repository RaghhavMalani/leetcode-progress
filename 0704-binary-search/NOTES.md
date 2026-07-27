# 704. Binary Search
> **Easy** &nbsp;·&nbsp; Binary search · exact match &nbsp;·&nbsp; family: **Binary search**

The template every other binary search is a mutation of. Three details carry all the weight: `<=` in the loop, `mid ± 1` in the updates, and the overflow-safe midpoint.

**▶ [Step through this solution line by line](../visualizations/0704-binary-search.html)** — 9 steps, traced on `nums = [-1,0,3,5,9,12], target = 9`.

| | |
|---|---|
| time | O(log n) |
| space | O(1) |

## The idea

Binary search is not "look in the middle". It is **maintaining an invariant while halving a range**. State the invariant explicitly — "if the answer exists, it is in [left, right]" — and every design decision (`<=` vs `<`, `mid` vs `mid ± 1`) follows from keeping it true.

## How to recognise it

- Sorted input plus a required O(log n).
- Much more broadly: **a monotone predicate**. If "is X good?" is false, false, false, true, true, true as X increases, you can binary search on X even when there is no array at all — that is binary-search-on-the-answer, and it is how LC 3620 in your repo works.
- "Minimum k such that…", "maximum capacity such that…", "smallest speed such that…" are all this pattern in disguise.

## Where people go wrong

- **`while left < right` with inclusive bounds.** Misses a single-element range. Inclusive bounds need `<=`.
- **`right = mid` instead of `mid - 1`.** With `<=` this is an infinite loop. Match your bound convention to your update.
- **`(left + right) // 2`.** Overflows in Java/C++ for large indices. The famous bug that sat in the JDK for nine years.
- **Trying to remember four variants.** Learn exactly two — this exact-match form, and the boundary form in the template — and derive everything else from them.

## The reusable template

```python
# Binary search - the invariant is "target, if present, is in [lo, hi]"
lo, hi = 0, len(a) - 1
while lo <= hi:                       # <= : the range [lo,hi] is INCLUSIVE
    mid = lo + (hi - lo) // 2         # never (lo+hi)//2 in a fixed-width language
    if a[mid] == target: return mid
    elif a[mid] < target: lo = mid + 1    # always +1 / -1, never mid
    else:                 hi = mid - 1
return -1

# Boundary search ("first index where pred is true") - a different, safer shape:
#   lo, hi = 0, n
#   while lo < hi:
#       mid = (lo + hi) // 2
#       if pred(mid): hi = mid
#       else:         lo = mid + 1
#   return lo
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| First / last occurrence of a value | Boundary form — do not stop on a match, keep shrinking towards the edge. |
| Insert position | LC 35 — return `left` after the loop ends. |
| **Rotated sorted array** | LC 33 / 81 — decide which half is sorted first, then test the target against it. Your repo has 81. |
| Binary search on the ANSWER | LC 875, 1011, 410, and LC 3620 in your repo. The array is the range of possible answers, and `check(mid)` is the predicate. |
| 2D sorted matrix | LC 74 — treat it as one flat sorted array of length m·n. |

## How to think about it next time

The upgrade that pays off most: stop thinking "binary search needs a sorted array" and start thinking **"binary search needs a monotone yes/no question"**. Once that clicks, a whole class of optimisation problems opens up — "what is the smallest capacity that works?" becomes "binary search the capacity, and write a linear `can(capacity)` checker". The hard part of those problems is never the search; it is writing `can()` and convincing yourself it is monotone.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/binary-search)
