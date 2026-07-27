# 3513. Number of Unique XOR Triplets I
> **Medium** &nbsp;·&nbsp; Bit reasoning · closed form &nbsp;·&nbsp; family: **Bit manipulation**

One line, O(1). The whole problem is the promise hidden in the statement: *nums is a permutation of 1..n*, which means the answer depends only on n.

**▶ [Step through this solution line by line](../visualizations/3513-number-of-unique-xor-triplets-i.html)** — 5 steps, traced on `nums = a permutation of [1,2,3,4]`.

| | |
|---|---|
| time | O(1) |
| space | O(1) |

## The idea

When the input is promised to be a **permutation of 1..n**, the array carries no information beyond n. Every question about its multiset therefore has an answer that is a function of n alone — and the job becomes proving what that function is, not writing a loop.

## How to recognise it

- The phrase "nums is a permutation of [1, n]" or "contains each of 1..n exactly once". Highlight it; it is never decorative.
- XOR reachability arguments: with the numbers 1..n you can produce every value in [0, 2^bits(n)), because each power of two below n is available and XOR lets you combine them freely.
- A brute force of O(n³) with n up to 10⁵ — the gap between that and the constraints tells you a closed form is expected.

## Where people go wrong

- **Enumerating triplets.** O(n³) times out immediately.
- **Off-by-one in `bit_length`.** `(4).bit_length()` is 3, and `1 << 3` = 8. Check n = 3 (bit_length 2 → 4) and n = 4 by hand.
- **Missing the n ≤ 2 guard.** The reachability argument needs at least three elements to work as stated.
- **Assuming the array order matters.** It never does when the input is a permutation of a fixed range.

## The reusable template

```python
# the input is a PERMUTATION of 1..n, so only n matters
if n <= 2:
    return n
return 1 << n.bit_length()      # every XOR value in [0, 2^bits) is reachable

# arbitrary array (part II)? no closed form:
#   pair_xors = {a ^ b for a in nums for b in nums}      # O(n^2)
#   answer    = len({p ^ c for p in pair_xors for c in nums})
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Part II** (LC 3514) | The array is arbitrary, so the closed form dies. You compute the set of pairwise XORs first, then XOR each with every element — O(n² + n·maxValue/64) with bitsets. |
| Unique XOR of PAIRS | Same style of reasoning, one order lower. |
| Maximum XOR of two numbers (LC 421) | A binary trie, built bit by bit from the top. |
| Count subarrays with XOR = k | Prefix XOR plus a hash map — the Two Sum trick again. |

## How to think about it next time

Read constraints as **information**, not just as size limits. "A permutation of 1..n", "all values distinct", "values ≤ 100", "the array is sorted" — each of these hands you a structural fact that can collapse the problem. When the stated brute force is wildly beyond the constraints, the intended solution is usually not a cleverer search but a proof that the answer has a closed form. Ask "what could the answer possibly depend on?" before you ask "how do I compute it faster?"

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/number-of-unique-xor-triplets-i)
