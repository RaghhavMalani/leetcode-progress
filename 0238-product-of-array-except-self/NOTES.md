# 238. Product of Array Except Self
> **Medium** &nbsp;·&nbsp; Prefix / suffix accumulation &nbsp;·&nbsp; family: **Prefix sums & intervals**

Prefix × suffix, with the output array doing double duty as scratch space. The load-bearing detail is writing to `res[i]` *before* folding `nums[i]` into the accumulator.

**▶ [Step through this solution line by line](../visualizations/0238-product-of-array-except-self.html)** — 20 steps, traced on `nums = [1,2,3,4]`.

| | |
|---|---|
| time | O(n) — two passes |
| space | O(1) extra, excluding the output |

## The idea

Anything of the form "combine everything except position i" splits into **a prefix part and a suffix part**. Compute prefixes forwards, suffixes backwards, and combine. It works for any associative operation — product, sum, XOR, max, gcd, matrix multiply.

## How to recognise it

- "For each i, some function of all the OTHER elements."
- An explicit ban on division (which would be the trivial answer, and breaks on zeros anyway).
- The O(1) space follow-up — the answer is "reuse the output array as the accumulator for one of the two passes".

## Where people go wrong

- **Updating the accumulator before writing.** Then `nums[i]` is included in its own answer. Write, then accumulate — in both passes.
- **Division.** `total // nums[i]` dies on a single zero, and gives garbage on two zeros. Even if allowed, mention this.
- **Counting the output as extra space.** The problem explicitly excludes it. Say so, otherwise it looks like you missed the constraint.
- **Two separate prefix and suffix arrays.** Correct, O(n) space, and a perfectly good first answer — then collapse one of them into a scalar.

## The reusable template

```python
# Prefix x suffix, O(1) extra space
res = [1] * n

prefix = 1
for i in range(n):
    res[i] = prefix          # WRITE first: excludes nums[i] from its own answer
    prefix *= nums[i]        # then accumulate

postfix = 1
for i in range(n - 1, -1, -1):
    res[i] *= postfix        # write first...
    postfix *= nums[i]       # ...then accumulate

# same shape for sum / XOR / max / gcd - any associative operation
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Sum except self | `total - nums[i]`, trivially. The product version is hard only because division is forbidden. |
| XOR except self | `total_xor ^ nums[i]` — XOR is its own inverse, so it collapses like sum. |
| Max except self | Prefix max and suffix max arrays; no inverse exists, so you cannot collapse to a scalar in one direction. |
| **Trapping Rain Water** (LC 42) | prefix-max × suffix-max in structure, then optimised further to two pointers. Also in your repo. |
| **Candy** (LC 135) | Two sweeps, left-to-right then right-to-left, taking a max. The same two-pass shape. |

## How to think about it next time

"Two passes, one forward and one backward" is a pattern worth naming for yourself. It solves this, trapping rain water, candy, LC 1840 in your repo, and any problem where each position depends on both what came before and what comes after. Whenever you catch yourself wanting to look both ways from every index, stop writing the O(n²) loop and ask: **can I sweep once in each direction and combine?**

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/product-of-array-except-self)
