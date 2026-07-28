# 168. Excel Sheet Column Title
> **Easy** &nbsp;&middot;&nbsp; Math · bijective base conversion &nbsp;&middot;&nbsp; family: **Math & number theory**

Base-26 with no zero digit. Every `-1` in these five lines is doing the same job: shifting a 1-based alphabet into the 0-based arithmetic that `%` and `//` expect.

**▶ [Step through this solution line by line](./visualization.html)** — 10 steps, traced on `columnNumber = 701`.

| | |
|---|---|
| time | O(log₂₆ n) |
| space | O(log₂₆ n) for the output |

## The idea

Ordinary base-b uses digits 0..b−1. A **bijective** base-b uses 1..b — there is no zero, so every positive integer has exactly one representation and no leading-zero ambiguity. Spreadsheet columns work this way: A, …, Z, AA, …, AZ, BA. Subtracting 1 before each `%` and `//` converts between the two systems.

## How to recognise it

- A counting system with **no zero symbol** — spreadsheet columns, some ID schemes, 1-indexed alphabets.
- The giveaway test case is the exact multiple: 26 must be "Z", not "A@" or "AZ". If your code gets 26 right it is almost certainly correct.
- General base conversion: repeated `%` for the digit, `//` to shrink, then reverse.

## Where people go wrong

- **Forgetting the −1.** The single bug in this problem. Test 26, 52, 676 — all the exact multiples.
- **Only subtracting 1 in one of the two places.** Both the modulo and the division need it.
- **Building the string forwards.** Digits come out least-significant first, so you must reverse (or prepend, which is O(n²) in Python).
- **Confusing this with the reverse direction.** LC 171 (title → number) is Horner’s method: `n = n*26 + (ord(c) - 64)`, and it needs no −1 at all.

## The reusable template

```python
# Bijective base 26 (digits 1..26, no zero)
res = ""
while n > 0:
    n -= 1                        # 1-based -> 0-based, ONCE, before both ops
    res += chr(ord('A') + n % 26)
    n //= 26
return res[::-1]

# ordinary base b: drop the -1 entirely
# the reverse direction (LC 171) is Horner:  n = n * 26 + (ord(c) - 64)
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Column title → number** (LC 171) | `n = n * 26 + (ord(c) - ord("A") + 1)`. No offset gymnastics. |
| Ordinary base conversion | Digits 0..b−1, so drop every −1. |
| Roman numerals (LC 12 / 13) | Not positional at all — a greedy table of value/symbol pairs. |
| Base 62 / URL shortening | Ordinary base conversion over [0-9a-zA-Z]. |

## How to think about it next time

When a problem involves 1-based indexing and modular arithmetic, **convert to 0-based at the boundary, do all the maths, convert back**. That is a general discipline, not a trick for this problem — it is why `(x - 1) % n` and `((x - 1) % n) + 1` show up all over circular-array and calendar code. Fixing the convention once at the edge beats scattering ±1 through the body.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/excel-sheet-column-title)
