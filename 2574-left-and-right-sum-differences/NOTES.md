# 2574. Left and Right Sum Differences
> **Easy** &nbsp;·&nbsp; Prefix sum · total minus prefix &nbsp;·&nbsp; family: **Prefix sums & intervals**

The suffix sum for free: `right = total - left - nums[i]`. No second array, no backward pass — worth internalising because it applies whenever the operation has an inverse.

**▶ [Step through this solution line by line](../visualizations/2574-left-and-right-sum-differences.html)** — 14 steps, traced on `nums = [10,4,8,3]`.

| | |
|---|---|
| time | O(n) |
| space | O(1) extra |

## The idea

A suffix aggregate can be derived from the total and the prefix **whenever the operation is invertible**. Sum has subtraction, XOR is its own inverse, product has division (if there are no zeros). Max and min have no inverse — which is exactly why LC 238 in your repo needs two passes and this one does not.

## How to recognise it

- You need "everything before i" and "everything after i" simultaneously.
- The combining operation is a sum, XOR, or count — something you can undo.
- If the operation is max/min/gcd, you cannot subtract; build a real suffix array (two passes).

## Where people go wrong

- **Forgetting to exclude nums[i].** right = total − left is wrong; it includes the current element.
- **Updating `left_sum` before writing the answer.** Same bug as LC 238 — write, then accumulate.
- **Building both prefix and suffix arrays.** Correct, O(n) space, and unnecessary here.
- **Recomputing `sum(nums)` inside the loop.** O(n²) by accident.

## The reusable template

```python
# invertible operation -> suffix comes free from the total
total, left = sum(nums), 0
for x in nums:
    right = total - left - x       # exclude x from BOTH sides
    ans.append(abs(left - right))
    left += x                      # accumulate AFTER the write

# not invertible (max, min, gcd)? build a real suffix array, two passes.
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Product** except self (LC 238) | Division is unsafe with zeros, so two passes. Also in your repo. |
| **Find Pivot Index** (LC 724) | Same identity, looking for where left == right. |
| Max on each side | No inverse — build prefix-max and suffix-max arrays. |
| **Trapping Rain Water** (LC 42) | Prefix-max and suffix-max, then optimised to two pointers. Also in your repo. |

## How to think about it next time

Whenever you need both sides of every index, ask one question: **is my operation invertible?** If yes, one pass plus a total. If no, two passes. That single question tells you immediately whether you need O(1) or O(n) extra space, and it distinguishes this problem from LC 238 despite them looking identical.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/left-and-right-sum-differences)
