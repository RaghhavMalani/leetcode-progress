# 70. Climbing Stairs
> **Easy** &nbsp;&middot;&nbsp; DP · Fibonacci with rolling variables &nbsp;&middot;&nbsp; family: **Dynamic programming**

Every dynamic programming problem starts here. Two things to take away: how to *find* the recurrence, and how to notice that a dp array of size n can collapse to two integers.

**▶ [Step through this solution line by line](./visualization.html)** — 17 steps, traced on `n = 6`.

| | |
|---|---|
| time | O(n) |
| space | O(1) — down from the O(n) of the obvious dp array |

## The idea

Find the recurrence by asking **"what was the last decision?"**. To be standing on step n you either just took a 1-step (from n−1) or a 2-step (from n−2). Those cases are disjoint and cover everything, so ways(n) = ways(n−1) + ways(n−2). That question — what was the last move? — generates the recurrence for most counting DPs.

## How to recognise it

- "How many ways to…" with a small set of moves. Counting → DP; listing them all → backtracking.
- The answer at n depends on a **fixed number of earlier answers**. That is what makes the space collapse possible.
- Overlapping subproblems: naive recursion recomputes ways(4) many times, which is the signal to memoise or go bottom-up.

## Where people go wrong

- **Plain recursion with no memo.** O(2ⁿ). It is the honest first answer, but say "and this recomputes, so I will memoise".
- **Base cases.** ways(0) = 1 (the empty climb) and ways(1) = 1. Setting ways(0) = 0 is the classic off-by-one that breaks everything downstream.
- **Overwriting `one` before saving it.** Hence the `temp`. Python lets you write `one, two = one + two, one` and skip it.
- **Keeping the whole dp array out of habit.** If the recurrence only reaches back k places, you only need k variables. Interviewers ask for this improvement almost every time.

## The reusable template

```python
# Fibonacci-shaped DP, rolled down to O(1) space
one, two = 1, 1                 # ways(1), ways(0)
for _ in range(n - 1):
    one, two = one + two, one   # slide the window forward
return one

# the array version you should write FIRST, then collapse:
#   dp = [0] * (n + 1); dp[0] = dp[1] = 1
#   for i in range(2, n + 1):
#       dp[i] = dp[i-1] + dp[i-2]
#   return dp[n]
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Steps of 1, 2 or 3 | Tribonacci — keep three variables. |
| **Min Cost Climbing Stairs** (LC 746) | Same recurrence with a min and a cost term instead of a sum. |
| **House Robber** (LC 198) | ways → max, and you skip the adjacent element. Structurally identical. |
| **Decode Ways** (LC 91) | Fibonacci-shaped, with validity conditions on each transition. |
| n up to 10¹⁸ | Matrix exponentiation, O(log n). LC 3700 in your repo uses exactly this technique. |

## How to think about it next time

Build every DP in four steps, out loud, before coding. **(1) What is the state?** "the step I am on". **(2) What is the recurrence?** — ask what the last decision was. **(3) What are the base cases?** **(4) In what order do I fill it?** Then, as a fifth step, ask **"how far back does the recurrence reach?"** — if the answer is a small constant, drop the array and use that many variables. Those five questions cover the overwhelming majority of DP problems you will be asked.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/climbing-stairs)
