# 90. Subsets II
> **Medium** &nbsp;·&nbsp; Backtracking · duplicate suppression &nbsp;·&nbsp; family: **Backtracking**

Problem 78 plus one while loop. Compare the tree here with the one on the Subsets page: two branches that would have been identical have been merged away.

**▶ [Step through this solution line by line](../visualizations/0090-subsets-ii.html)** — 43 steps, traced on `nums = [1,2,2]`.

| | |
|---|---|
| time | O(2ⁿ · n) worst case (all distinct) |
| space | O(n) depth |

## The idea

Identical to problem 40 minus the sum target. That is worth internalising: **40 : 39 :: 90 : 78**. The duplicate-suppression machinery is completely orthogonal to what the problem is actually counting, which is why the same four lines transplant cleanly.

## How to recognise it

- Power set / combinations, input **may contain duplicates**, output rows must be unique.
- The moment you see "may contain duplicates" in a subset or combination problem, write `sort()` before you write anything else.

## Where people go wrong

- **No sort.** The while loop compares neighbours and does nothing if equal values are scattered.
- **Skipping on the take branch.** [2,2] is a legitimate subset; you must be able to take both.
- **Trying to dedupe with a set of tuples.** It passes, but it does the full 2ⁿ work first.
- **Writing `i += 1` inside a loop over a parameter and expecting the caller to see it** — it is a local rebinding, which is exactly what you want here, but people sometimes assume the opposite.

## The reusable template

```python
# sort + skip equal neighbours on the SKIP branch
nums.sort()
path.append(nums[i]); backtrack(i+1); path.pop()   # take branch
while i+1 < len(nums) and nums[i] == nums[i+1]:
    i += 1
backtrack(i+1)          # skip branch now lands on a NEW value
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| No duplicates in input | LC 78 — drop the while loop. |
| With a sum target | LC 40 — add the total and the two guards. |
| Permutations with duplicates | LC 47 — counter idiom instead. |
| Count distinct subsets only | Multiply (count[v]+1) over distinct values. No search at all. |

## How to think about it next time

Build yourself a two-axis grid: rows = {subsets, combinations with a target, permutations}, columns = {distinct input, duplicate input}. Six cells, and you have solved five of them (78, 39, 46, 90, 40, 47). Being able to say which cell a new problem sits in — before writing code — is most of what interviewers are testing when they hand you one of these.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/subsets-ii)
