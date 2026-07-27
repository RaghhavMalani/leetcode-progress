# 3699. Number of Zigzag Arrays I
> **Hard** &nbsp;·&nbsp; DP with direction state + prefix-sum transitions &nbsp;·&nbsp; family: **Dynamic programming**

Two lessons: the state you need is "last value + last direction", and a transition that sums over a range collapses from O(m) to O(1) with a running prefix sum.

**▶ [Step through this solution line by line](../visualizations/3699-number-of-zigzag-arrays-i.html)** — 13 steps, traced on `n = 3, l = 4, r = 5`.

| | |
|---|---|
| time | O(n · m) where m = r − l + 1 |
| space | O(m) |

## The idea

Two techniques stacked. **(1) State design:** to extend a zigzag you need only the last value and the last direction — nothing earlier matters, so the state is 2m rather than exponential. **(2) Prefix-sum transitions:** the natural transition is "sum over all smaller values", which is O(m) per state and O(m²) per length. Accumulating a running prefix as you sweep makes each transition O(1).

## How to recognise it

- Counting sequences with an **alternating** or local-comparison constraint — zigzag, wiggle, strictly alternating parity.
- A DP transition of the form `dp[x] = Σ dp'[y] for y < x` — that shape is *always* a prefix sum in disguise.
- Value ranges compressed to 1..m because only relative order matters.

## Where people go wrong

- **Writing the O(m²) transition and stopping.** Correct but too slow; the prefix sum is the intended optimisation and the whole point of the problem.
- **Sweep direction.** `new_up` needs a PREFIX (smaller values) so you sweep left to right; `new_down` needs a SUFFIX so you sweep right to left. Mixing them is the easiest bug to introduce here.
- **Adding to the prefix before writing.** `new_up[x] = prefix` must come before `prefix += down[x]`, or x counts itself. Same discipline as LC 238 in your repo.
- **The base case.** Length 2, not 1 — hence the loop starting at 3.
- **Forgetting the modulus** inside the accumulation, not just at the end.

## The reusable template

```python
# state: (last value, last direction). transition: sum over a RANGE -> prefix sum.
up   = [x - 1 for x in range(m + 1)]     # base: length-2 arrays ending going UP
down = [m - x for x in range(m + 1)]

for _ in range(3, n + 1):
    new_up, new_down = [0] * (m + 2), [0] * (m + 2)

    pre = 0
    for x in range(1, m + 1):            # LEFT to RIGHT: needs smaller values
        new_up[x] = pre                  # write BEFORE accumulating
        pre = (pre + down[x]) % MOD

    suf = 0
    for x in range(m, 0, -1):            # RIGHT to LEFT: needs larger values
        new_down[x] = suf
        suf = (suf + up[x]) % MOD

    up, down = new_up, new_down

return (sum(up) + sum(down)) % MOD
# n up to 1e18? the transition is linear -> matrix exponentiation (part II).
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Part II** (LC 3700) | n up to 10¹⁸ — the transition is linear, so use **matrix exponentiation** for O(m³ log n). Also in your repo. |
| **Wiggle Subsequence** (LC 376) | Longest zigzag rather than a count — greedy, O(n). |
| **Count Vowel Permutations** (LC 1220) | Same "state = last symbol" DP with a fixed transition table. |
| Strictly increasing arrays | Drop the direction state; the transition is a plain prefix sum. |

## How to think about it next time

Two questions to run on every DP. **First: what is the minimal state?** Here, "last value and last direction" — anything more is waste, anything less is insufficient. **Second: is my transition summing over a contiguous range?** If so, replace the inner loop with a running prefix or suffix sum and drop a whole factor. Those two questions turn most Hard counting DPs into Medium ones, and the second one in particular is the difference between accepted and TLE far more often than the state design is.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/number-of-zigzag-arrays-i)
