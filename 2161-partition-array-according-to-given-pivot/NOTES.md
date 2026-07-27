# 2161. Partition Array According to Given Pivot
> **Medium** &nbsp;·&nbsp; Stable three-way partition &nbsp;·&nbsp; family: **Two pointers & sliding window**

Compare this directly with Sort Colors (LC 75) in your repo. Same three-way split — but here **stability is required**, and that one word forbids the in-place swapping trick entirely.

**▶ [Step through this solution line by line](../visualizations/2161-partition-array-according-to-given-pivot.html)** — 16 steps, traced on `nums = [9,12,5,10,14,3,10], pivot = 10`.

| | |
|---|---|
| time | O(n) |
| space | O(n) — required, because stability rules out in-place swaps |

## The idea

**Stability** — preserving the original relative order of equal-category elements — is a real constraint with a real cost. The Dutch-flag partition in LC 75 is O(1) space precisely because it is free to fling elements across the array; the moment order matters, you must build the output in reading order, which needs O(n).

## How to recognise it

- "Preserve the relative order" / "the same order as in nums" in the statement. Read for this phrase specifically — it changes the answer.
- Any grouping where the within-group order carries meaning (records, timestamps, tie-breaks).
- If the statement says nothing about order, prefer the O(1) in-place version and say why you can.

## Where people go wrong

- **Porting the LC 75 solution.** It passes the "are they grouped?" check and fails the order check. The two problems look identical and are not.
- **Sorting.** O(n log n), and Python’s sort is stable so it would work — but it does far more than asked.
- **Two lists instead of three.** You need the equal bucket separately; merging it into either side breaks the ordering guarantee.
- **Claiming O(1) space.** The output is O(n) and so is the intermediate; be honest about it.

## The reusable template

```python
# STABLE three-way partition: build in reading order, O(n) space
less, equal, greater = [], [], []
for x in nums:
    (less if x < pivot else equal if x == pivot else greater).append(x)
return less + equal + greater

# order does NOT matter? then Dutch flag in place, O(1) space (LC 75):
#   low = mid = 0; high = n-1
#   while mid <= high: ...swap...      <- destroys relative order
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Sort Colors** (LC 75) | No stability requirement → Dutch flag, O(1) space. Also in your repo. |
| **Move Zeroes** (LC 283) | Stable two-way partition, and it CAN be done in place with a single write pointer. |
| **Odd Even Linked List** (LC 328) | Stable partition on a list — two chains, then splice. |
| Quicksort partition | Unstable by design; that is what makes it in place. |

## How to think about it next time

Build the habit of reading constraints for words that **change the algorithm class**: "in place", "preserve order", "without extra space", "one pass", "do not modify the input". Each of those rules out a family of solutions. Here, "preserve order" alone turns an O(1)-space problem into an O(n)-space one — and noticing it before you code saves you from confidently submitting the wrong classic.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/partition-array-according-to-given-pivot)
