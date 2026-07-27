# 1071. Greatest Common Divisor of Strings
> **Easy** &nbsp;·&nbsp; Number theory analogy · gcd on lengths &nbsp;·&nbsp; family: **Math & number theory**

Your solution scans candidate lengths downwards. There is a two-line version built on a lovely fact: a common divisor string exists *iff* `s1 + s2 == s2 + s1`, and its length is exactly `gcd(len(s1), len(s2))`.

**▶ [Step through this solution line by line](../visualizations/1071-greatest-common-divisor-of-strings.html)** — 5 steps, traced on `str1 = "ABCABC", str2 = "ABC"`.

| | |
|---|---|
| time | O(min(l1,l2) × (l1+l2)) as written; O(l1+l2) with the gcd trick |
| space | O(l1+l2) |

## The idea

Strings under concatenation behave like integers under addition, and "divides" transfers exactly. Two consequences: **(1)** if any common divisor string exists, its length must divide both lengths, so the longest has length `gcd(l1, l2)`; **(2)** a common divisor exists at all iff `s1 + s2 == s2 + s1` — that is, the two strings commute.

## How to recognise it

- "Repeated pattern", "X divides Y", "smallest repeating unit". All of these are gcd/period questions in disguise.
- The related classic: the smallest period of a string is `n - failure[n-1]` from the KMP failure function.
- Whenever lengths must divide each other, gcd is lurking.

## Where people go wrong

- **Forgetting the divisibility pre-check.** Line 7 rejects most candidates in O(1) before doing any O(n) string comparison — without it this is much slower.
- **Not checking the commuting condition** in the fast version. `s1 + s2 != s2 + s1` means no divisor exists at all, and you must return "" rather than a gcd-length prefix.
- **Assuming the answer is always a prefix of the shorter string.** It is, but only because a divisor of both must be a prefix of both — say why.
- **Scanning upwards.** Then you must not return on the first success, and you would do more work.

## The reusable template

```python
# the two-line version
from math import gcd

def gcdOfStrings(s1, s2):
    if s1 + s2 != s2 + s1:          # they must COMMUTE, or no divisor exists
        return ""
    return s1[:gcd(len(s1), len(s2))]

# why: strings under concatenation behave like integers under addition.
# any common divisor's length divides both lengths -> the longest is gcd.
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Repeated Substring Pattern** (LC 459) | Is s made of a repeated unit? `s in (s+s)[1:-1]`, or use the KMP failure function. |
| Smallest repeating unit | `n - failure[n-1]` if it divides n, else n. |
| gcd of an array of strings | Fold the pairwise gcd across the list. |
| **Find GCD of Array** (LC 1979) | The integer version — gcd(min, max). Also in your repo. |

## How to think about it next time

When a problem uses arithmetic vocabulary — divides, multiple, common, greatest — for a non-numeric object, **check whether the analogy is exact**. Here it is: concatenation is associative with an identity (the empty string), so divisibility, gcd and lcm all carry over. Recognising an algebraic structure you already know is one of the highest-leverage moves available, because you get its entire toolkit for free.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/greatest-common-divisor-of-strings)
