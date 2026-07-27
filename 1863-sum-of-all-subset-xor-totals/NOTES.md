# 1863. Sum of All Subset XOR Totals
> **Easy** &nbsp;·&nbsp; Bit counting · contribution technique &nbsp;·&nbsp; family: **Bit manipulation**

Marked Easy because backtracking passes. The real solution is one line, and it comes from asking a different question: not "what is each subset worth?" but "how often does each *bit* appear?"

**▶ [Step through this solution line by line](../visualizations/1863-sum-of-all-subset-xor-totals.html)** — 6 steps, traced on `nums = [5,1,6]`.

| | |
|---|---|
| time | O(n) |
| space | O(1)  — versus O(2ⁿ · n) for enumeration |

## The idea

The **contribution technique**: instead of computing each object’s value and summing, compute how much each *component* contributes across all objects. Here, fix a bit b that some number has. Split the numbers into those with bit b set and those without. Exactly half of all subsets contain an odd count of the former, so bit b is set in exactly 2ⁿ⁻¹ of the XOR totals — regardless of anything else.

## How to recognise it

- "Sum over all subsets / subarrays / pairs" — the answer is nearly always a contribution argument, not enumeration.
- Bitwise operations plus a sum. Bits are independent, so you can handle each position separately and add up.
- Constraints small enough for brute force (n ≤ 12 here) are often a deliberate red herring — the elegant solution is what the problem is really about.

## Where people go wrong

- **n = 1.** Then 2ⁿ⁻¹ = 2⁰ = 1 and the formula still holds. Check it — off-by-one exponents are the usual bug here.
- **Using XOR instead of OR to accumulate.** You want "which bits appear anywhere", which is OR. XOR would cancel pairs.
- **Thinking half the subsets means half the numbers.** The argument is about subsets, and it holds for every bit independently.
- **Writing the backtracking version and stopping there.** It passes; it also misses the entire lesson.

## The reusable template

```python
# contribution technique: count how often each COMPONENT appears
# sum over all 2^n subsets of XOR(subset)  ==  OR(nums) * 2^(n-1)
res = 0
for n in nums:
    res |= n                      # which bits appear ANYWHERE
return res * 2 ** (len(nums) - 1)

# why: for any bit set in some number, exactly half of all subsets contain
# an ODD number of the elements having that bit -> it survives the XOR in
# 2^(n-1) subsets. Same argument gives sum-of-subset-SUMS = sum * 2^(n-1).
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Sum of subarray minimums** (LC 907) | Contribution again: count for how many subarrays each element is the minimum, using a monotonic stack. |
| **Sum of subarray ranges** (LC 2104) | Max contributions minus min contributions. |
| Count of set bits in 0..n | LC 338 — per-bit counting once more. |
| Sum of all subset SUMS | Each element appears in 2ⁿ⁻¹ subsets, so the answer is `sum(nums) × 2ⁿ⁻¹`. Same argument, different operation. |

## How to think about it next time

When you see "sum over all X", **flip the order of summation**. Instead of Σ over objects of (value of object), compute Σ over components of (component × how many objects contain it). That single reversal turns exponential enumeration into a counting problem, and it is the key to a whole tier of problems that look impossible at first — subarray minimums, subarray ranges, pairwise distances, and this one.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/sum-of-all-subset-xor-totals)
