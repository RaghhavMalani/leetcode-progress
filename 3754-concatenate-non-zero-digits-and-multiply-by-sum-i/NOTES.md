# 3754. Concatenate Non-Zero Digits and Multiply by Sum I
> **Easy** &nbsp;·&nbsp; Digit manipulation · single pass, two accumulators &nbsp;·&nbsp; family: **Math & number theory**

Straight simulation. Two things worth noting: both accumulators are built in one pass, and the empty-string guard is a real edge case, not decoration.

**▶ [Step through this solution line by line](../visualizations/3754-concatenate-non-zero-digits-and-multiply-by-sum-i.html)** — 11 steps, traced on `n = 3049`.

| | |
|---|---|
| time | O(d) in the digit count |
| space | O(d) |

## The idea

Digit problems come in two flavours: **string-based** (easy to index, easy to concatenate, easy to reverse) and **arithmetic** (`% 10` and `// 10`, no allocation, works when the number is too big to stringify comfortably). Pick the one that matches the operation — here concatenation makes strings the obvious choice.

## How to recognise it

- Anything that inspects, filters or reorders decimal digits.
- If you need the digits **in order**, strings win; if you only need them one at a time, `divmod(n, 10)` avoids the allocation but yields them backwards.
- Several independent accumulations over one input → one pass, several variables. Do not loop twice out of habit.

## Where people go wrong

- **Forgetting the all-zeros case.** `int("")` raises ValueError. n = 0, or n = 1000 after filtering, both hit it.
- **Building the string backwards** by using `divmod` and forgetting to reverse.
- **Two separate loops** for the string and the sum. Correct, but the one-pass version is shorter and shows intent.
- **Leading zeros.** Here they are stripped by construction; in general `int("007")` is 7, which may or may not be what you want.

## The reusable template

```python
# one pass, two accumulators, and guard the empty case
s = str(n)
kept, digit_sum = "", 0
for ch in s:
    if ch != '0':
        kept += ch
        digit_sum += int(ch)

if not kept:            # every digit was zero -> int("") would raise
    return 0
return int(kept) * digit_sum

# arithmetic alternative (yields digits BACKWARDS):
#   while n: n, d = divmod(n, 10); ...
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Sum of digits only | `sum(int(c) for c in str(n))`, or the `divmod` loop. |
| Reverse an integer | LC 7 — `divmod` loop, plus an overflow check in fixed-width languages. |
| **Excel column title** (LC 168) | Base-26 digit construction. Also in your repo. |
| **Total Waviness** (LC 3751 / 3753) | Digit DP over the same string representation. Also in your repo, and far harder. |

## How to think about it next time

When several quantities must be derived from one traversal, **compute them all in the same loop**. It is not just about speed — it keeps the invariants visibly in sync and stops you from accidentally filtering differently in the two passes. And whenever a problem builds a value from a filtered subset, ask immediately: *what if the subset is empty?* That question catches most edge-case failures in easy problems.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i)
