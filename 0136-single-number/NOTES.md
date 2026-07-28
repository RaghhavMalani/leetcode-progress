# 136. Single Number
> **Easy** &nbsp;&middot;&nbsp; Bit manipulation · XOR cancellation &nbsp;&middot;&nbsp; family: **Bit manipulation**

The cleanest use of XOR there is. Because `x ^ x = 0` and order does not matter, folding XOR across the array annihilates every pair and leaves the singleton.

**▶ [Step through this solution line by line](./visualization.html)** — 7 steps, traced on `nums = [4,1,2,1,2]`.

| | |
|---|---|
| time | O(n) |
| space | O(1) |

## The idea

XOR is addition modulo 2, bit by bit, with no carry. Its three properties — self-inverse, identity 0, commutative/associative — mean that XOR-ing a whole collection is a **parity check on every bit position at once**. Anything that appears an even number of times vanishes.

## How to recognise it

- "Every element appears twice except one" — or any even/odd count phrasing.
- O(1) space demanded, ruling out a set or a counter.
- Also: find a missing number (XOR the values with the indices), detect a swapped pair, toggle a flag, check parity.

## Where people go wrong

- **Assuming it generalises to triples.** With every element appearing three times (LC 137), XOR does not cancel. You need per-bit counting mod 3, or the two-mask trick.
- **Two singletons.** LC 260 — the total XOR gives `a ^ b`; isolate any set bit with `x & -x` and partition on it.
- **Using a set or a Counter.** Correct, and fine to say first, but O(n) space.
- **Forgetting XOR’s identity.** Starting `res` at anything other than 0 corrupts the answer.

## The reusable template

```python
# XOR fold - everything paired cancels
res = 0
for n in nums:
    res ^= n
return res

# the identities worth memorising
#   x ^ x == 0          x ^ 0 == x         XOR is commutative + associative
#   x & (x - 1)         clears the lowest set bit
#   x & -x              isolates the lowest set bit
#   x >> k & 1          read bit k          x | (1 << k)   set bit k
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Every element appears three times (LC 137) | Count each bit mod 3, or the `ones/twos` two-mask trick. |
| **Two** single numbers (LC 260) | XOR everything, isolate the lowest set bit, split into two groups. |
| **Missing Number** (LC 268) | XOR all values with all indices — the pairs cancel and the missing index survives. |
| **Find the Duplicate** (LC 287) | XOR does not help; use Floyd. Also in your repo. |
| **Sum of subset XOR totals** (LC 1863) | Each bit is set in exactly half the subsets → `OR(nums) * 2^(n-1)`. Also in your repo. |

## How to think about it next time

Keep a short list of bit identities in working memory: `x ^ x = 0`, `x ^ 0 = x`, `x & (x-1)` clears the lowest set bit, `x & -x` isolates it, `x | (1<<k)` sets a bit, `x >> k & 1` reads one. Almost every bit problem is one of these applied once. And the meta-signal: **when a problem demands O(1) space on integer data, bits are usually the intended route.**

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/single-number)
