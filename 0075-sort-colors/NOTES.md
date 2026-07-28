# 75. Sort Colors
> **Medium** &nbsp;&middot;&nbsp; Three pointers · Dutch national flag &nbsp;&middot;&nbsp; family: **Two pointers & sliding window**

Dijkstra’s Dutch national flag partition. The only subtle line is the last one: after swapping with `high` you must NOT advance `mid`, because the incoming value is unexamined.

**▶ [Step through this solution line by line](./visualization.html)** — 20 steps, traced on `nums = [2,0,2,1,1,0]`.

| | |
|---|---|
| time | O(n) — one pass, no comparison sort |
| space | O(1) — in place |

## The idea

Partition an array into three regions in one pass by maintaining **loop invariants** on three pointers. The key mental discipline is naming exactly what each region means and checking that every branch preserves those meanings. Do that and the "why no `mid++`" question answers itself.

## How to recognise it

- Only a **small fixed number of distinct values** (here 3). With k values you can do k-way partition in O(n).
- The follow-up "can you do it in one pass with constant space?" — the two-pass counting-sort answer is the obvious one and this is the intended improvement.
- More generally: any "move all X to the front and all Y to the back" phrasing.

## Where people go wrong

- **Advancing `mid` after the 2-swap.** The single most common bug. The value swapped in from `high` has never been seen; skipping it can leave a 0 stranded in the middle.
- **`while mid < high` instead of `<=`.** Drops the last unexamined element.
- **Reaching for `sort()`.** Correct and O(n log n), but the problem exists specifically to test the linear partition.
- **Two-pass counting sort.** Perfectly valid, and worth offering first — but say "and I can do it in one pass" immediately after.

## The reusable template

```python
# Dutch national flag - three-way partition
# invariant: [0,low) = LOW   [low,mid) = MID   [mid,high] = unknown   (high,n) = HIGH
low = mid = 0
high = len(a) - 1
while mid <= high:
    if a[mid] < pivot:
        a[low], a[mid] = a[mid], a[low]; low += 1; mid += 1
    elif a[mid] == pivot:
        mid += 1
    else:
        a[mid], a[high] = a[high], a[mid]; high -= 1    # NO mid += 1
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Move Zeroes** (LC 283) | Two regions instead of three — a single write pointer. |
| Quicksort partition | Same idea with a pivot value; three-way partition is how you make quicksort survive many duplicate keys. |
| k distinct values, k > 3 | Pointers stop scaling — counting sort in two passes is the right answer. |
| **Partition Array According to Pivot** (LC 2161) | Order within each region must be preserved, so the in-place swap breaks it — you need three lists. Your repo has that one too. |

## How to think about it next time

This problem is really a lesson in **loop invariants**. Before writing the loop, write down (in a comment, honestly) what each region means. Then for each branch ask: "after this branch, are all four statements still true?" The 2-case fails that check if you advance mid, and you discover it on paper instead of in a failing test. That habit is worth far more than memorising this particular problem — it is how you debug any in-place pointer algorithm.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/sort-colors)
