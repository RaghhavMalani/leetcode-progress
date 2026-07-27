# 1846. Maximum Element After Decreasing and Rearranging
> **Medium** &nbsp;·&nbsp; Greedy · sort then climb &nbsp;·&nbsp; family: **Greedy**

Three lines that look too simple to be right. The argument: the optimal array is always 1, 2, 3, …, so sort and let each element climb one step if it can.

**▶ [Step through this solution line by line](../visualizations/1846-maximum-element-after-decreasing-and-rearranging.html)** — 11 steps, traced on `arr = [100,1,1000,1]`.

| | |
|---|---|
| time | O(n log n) — the sort |
| space | O(1) |

## The idea

Two observations collapse the problem. **(1)** Since you may only decrease, the best array is the steepest legal staircase: 1, 2, 3, …. **(2)** After sorting, giving each element the largest value it can legally take is optimal — using a smaller value never helps a later element, since later elements are ≥ this one.

## How to recognise it

- Operations that only go one direction (decrease-only, remove-only) plus free rearrangement. That combination almost always means "sort, then be greedy".
- "Maximise the maximum" / "maximise the final value" phrasings.
- If you could also *increase* values, the problem would be trivially `len(arr)`.

## Where people go wrong

- **Forgetting to sort.** The greedy is only valid on sorted input; unsorted it gives nonsense.
- **`ans = arr[0]` or `ans = 1` initially.** Starting at 0 makes the first element climb to 1 automatically, which is exactly the required arr[0] == 1.
- **Using `>=`.** Equal values cannot climb — [1,1] must become [1,1], not [1,2].
- **Over-thinking it into a DP.** Once you believe the staircase argument, there is nothing left to optimise.

## The reusable template

```python
# decrease-only + rearrange -> the answer is a 1,2,3,... staircase
arr.sort()
ans = 0
for x in arr:
    if x > ans:        # strictly greater: it can be decreased to ans+1
        ans += 1
return ans
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Minimum Replacements to Sort** (LC 2450) | Also decrease-only, but you split elements — greedy from the RIGHT. Also in your repo. |
| **Maximum Ice Cream Bars** (LC 1833) | Sort ascending and buy greedily. Also in your repo. |
| **Non-decreasing Array** (LC 665) | One change allowed — a case analysis, not a sweep. |
| Increases also allowed | Answer is `len(arr)`. Worth stating to show you understand which constraint is binding. |

## How to think about it next time

When a problem allows an operation in **only one direction**, that asymmetry is usually the whole solution. Decrease-only → sort ascending, climb greedily. Remove-only → keep as much as possible. Increase-only → sort descending. Ask "what does this restriction forbid me from fixing later?" — the answer tells you which order to process in, and the order is usually the algorithm.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging)
