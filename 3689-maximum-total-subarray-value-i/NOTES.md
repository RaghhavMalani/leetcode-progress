# 3689. Maximum Total Subarray Value I
> **Medium** &nbsp;·&nbsp; Observation · the constraint that is not there &nbsp;·&nbsp; family: **Greedy**

A one-line solution whose entire content is a reading-comprehension point: the k subarrays need not be *distinct*. Once you notice that, there is nothing left to compute.

**▶ [Step through this solution line by line](../visualizations/3689-maximum-total-subarray-value-i.html)** — 4 steps, traced on `nums = [1,3,2], k = 3`.

| | |
|---|---|
| time | O(n) |
| space | O(1) |

## The idea

Two observations. **(1) Monotone range:** extending a subarray can only increase max and decrease min, so (max − min) is maximised by the whole array. **(2) No distinctness constraint:** the k choices are independent, so all k should be that same best subarray. Multiply.

## How to recognise it

- A problem that looks like it needs DP over k choices — check first whether the choices actually interact.
- The words "distinct", "different", "non-overlapping" are **load-bearing**. Their absence is as informative as their presence.
- When the answer to "what is the single best option?" is easy and the options do not interact, the answer is k times that.

## Where people go wrong

- **Assuming the subarrays must be distinct.** Then it becomes a genuinely hard problem (that is part II). Reading it in is the trap.
- **Writing DP over (index, subarrays used).** Correct-ish, far slower, and it signals you missed the observation.
- **Overflow in a fixed-width language.** k and the range can both be large; use 64-bit.

## The reusable template

```python
return k * (max(nums) - min(nums))

# WHY: (max - min) over a subarray is maximised by the WHOLE array
# (extending never narrows the range), and the k picks are independent
# because nothing says they must be distinct. So: k copies of the best one.
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Subarrays must be **distinct** | Genuinely hard — you need the k largest distinct ranges, which is a different problem entirely. |
| Subarrays must be non-overlapping | Now they interact → DP or greedy with a sweep. |
| Maximise Σ max instead of Σ (max − min) | Same argument: k × max(nums). |
| **Sum of subarray ranges** (LC 2104) | Sum over ALL subarrays — contribution technique with a monotonic stack. |

## How to think about it next time

Read the constraints as carefully as the question. Specifically hunt for **constraints that are absent**: may I reuse? may they overlap? must they be distinct? must the answer be an actual index? Each absent restriction can collapse a problem by an entire complexity class. When a problem looks disproportionately hard for its rating, the usual explanation is that you imported a constraint that was never stated.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/maximum-total-subarray-value-i)
