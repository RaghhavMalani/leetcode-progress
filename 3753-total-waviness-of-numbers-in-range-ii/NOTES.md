# 3753. Total Waviness of Numbers in Range II
> **Hard** &nbsp;&middot;&nbsp; Digit DP · tight / started / carried context &nbsp;&middot;&nbsp; family: **Dynamic programming**

The canonical digit DP, with one extra twist: the recursion returns a *pair* — how many numbers, and how much waviness — because a peak at this position adds 1 to every number below it.

**▶ [Step through this solution line by line](./visualization.html)** — 10 steps, traced on `num1 = 1, num2 = 132`.

| | |
|---|---|
| time | O(digits × 2 × 2 × 10 × 10 × 10) — constant for any range |
| space | O(same) for the memo |

## The idea

Digit DP counts numbers with a property over an enormous range by **building them digit by digit** and memoising on a small state. Three components are near-universal: **tight** (still hugging the upper bound), **started** (leading zeros not yet broken), and whatever **context** the property needs — here the previous two digits.

## How to recognise it

- Ranges up to 10¹⁵ or larger, with a property defined on the **decimal digits** of each number.
- "Count numbers in [L, R] such that …" — always reduce to `f(R) − f(L−1)`.
- If the property needs the last k digits, the state carries k of them and the memo grows by 10^k.

## Where people go wrong

- **Forgetting `started`.** Leading zeros get treated as real digits and 007 registers a spurious valley.
- **Propagating `tight` wrongly.** It is `tight and (digit == limit)` — once you go below the bound you are free forever.
- **Memoising while `tight` is true.** Legal only because `tight` is part of the key. Leave it out of the key and the cache returns answers computed under a different bound.
- **Adding `add` instead of `add × child_count`.** The single hardest line. A peak at this position contributes 1 to EVERY number completed below it, not 1 in total.
- **Off-by-one at the lower end.** It is `solve(num1 - 1)`, and `solve(0)` must be well defined.
- **Recursion depth and cache size.** Fine at 16 digits, but clear the cache between the two `solve` calls — the bound differs.

## The reusable template

```python
# digit DP: three slots -> tight, started, context
def solve(n):                      # counts over [0, n]
    s = str(n)

    @lru_cache(None)               # tight/started MUST be part of the key
    def dfs(pos, tight, started, ctx):
        if pos == len(s):
            return (1, 0) if started else (0, 0)

        limit = int(s[pos]) if tight else 9      # tight -> capped by the bound
        cnt = tot = 0
        for d in range(limit + 1):
            ntight = tight and (d == limit)      # go below -> free forever
            if not started and d == 0:
                c, t = dfs(pos + 1, ntight, False, EMPTY_CTX)   # leading zero
            else:
                add = 1 if <property holds at this position> else 0
                c, t = dfs(pos + 1, ntight, True, next_ctx(ctx, d))
                t += add * c        # <- x c, NOT + add. one per completion.
            cnt += c; tot += t
        return cnt, tot

    return dfs(0, True, False, EMPTY_CTX)[1]

return solve(R) - solve(L - 1)     # prefix difference
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Count numbers without a digit 4 | The simplest digit DP — state is just (pos, tight). |
| Count numbers whose digit sum is divisible by k | Carry the running sum mod k. |
| **Numbers At Most N Given Digit Set** (LC 902) | Digit DP with a restricted alphabet. |
| **Count Special Integers** (LC 2376) | Add a bitmask of used digits to the state. |
| Sum of numbers rather than a count | Return (count, sum) — the same pair-returning structure as here. |

## How to think about it next time

Digit DP is a **template with three slots**: tight, started, and context. Learn it once, and then every problem in the family is just deciding what goes in the context slot — the last digit, the last two digits, a running remainder, a bitmask of used digits. The second, harder lesson from this problem is the **pair return**: when you need both a count and an aggregate, return them together, and remember that a per-node contribution must be multiplied by the number of completions beneath it. That multiply-by-count rule shows up in every "sum over all valid objects" tree recursion.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii)
