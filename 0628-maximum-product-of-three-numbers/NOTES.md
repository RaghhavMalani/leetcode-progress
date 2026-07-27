# 628. Maximum Product of Three Numbers
> **Easy** &nbsp;·&nbsp; Sorting · exhaustive case analysis &nbsp;·&nbsp; family: **Math & number theory**

Easy to code, easy to get wrong. The trap is forgetting that two large negatives multiply to a large positive — so the answer is not always "the three biggest".

**▶ [Step through this solution line by line](../visualizations/0628-maximum-product-of-three-numbers.html)** — 4 steps, traced on `nums = [-100,-98,-1,2,3,4]`.

| | |
|---|---|
| time | O(n log n) from the sort; O(n) is achievable — see below |
| space | O(1) |

## The idea

When the search space collapses to a **tiny number of candidates**, enumerate them and take the best. The skill is proving the list is exhaustive. Here: signs must multiply to positive, so the triple is either three positives (take the largest three) or one positive and two negatives (take the largest positive and the two most negative).

## How to recognise it

- "Maximum/minimum product/sum of exactly k elements" with small k.
- The presence of **negative numbers** in the constraints. If the problem says all values are positive, the case analysis vanishes and it is trivial.
- Any time sorting reduces a search to checking a couple of positions, that is the pattern.

## Where people go wrong

- **Only checking the three largest.** Fails on [-100,-98,-1,2,3,4]: the right answer is (−100)(−98)(4) = 39200, not 2·3·4 = 24.
- **Checking `nums[0]*nums[1]*nums[2]`.** The three most negative multiply to a negative — never optimal for a maximum.
- **Sorting when you do not need to.** A single pass tracking the three largest and two smallest is O(n). Worth offering as the improvement.
- **Overflow.** Irrelevant in Python; in Java/C++ three values near 10³ are fine but say you checked.

## The reusable template

```python
# Small candidate set + a proof that it is exhaustive
nums.sort()
return max(nums[-1] * nums[-2] * nums[-3],    # three largest
           nums[0]  * nums[1]  * nums[-1])    # two most negative + largest

# O(n) version: one pass tracking max1 >= max2 >= max3 and min1 <= min2
# WHY only two cases: the product must be positive, so the sign pattern is
# (+,+,+) or (+,-,-). Within each, take the largest magnitudes available.
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Maximum product of **two** numbers | max(largest × second-largest, smallest × second-smallest). |
| Maximum product of k numbers | Sort, then compare taking pairs from the negative end against singles from the positive end. The case analysis grows. |
| **Maximum Product Subarray** (LC 152) | Contiguous — completely different. DP tracking both the running max AND min, because a negative flips them. |
| **Maximum Product of Two Elements** (LC 1464) | All values positive, so no case analysis. Also in your repo. |

## How to think about it next time

Two habits. First: **when negatives are allowed, always ask what a negative does to your comparison.** Multiplication flips ordering; that single fact generates the second candidate here and the min-tracking in LC 152. Second: when the candidate set is small, say out loud *why* it is exhaustive. "The three biggest, or the two smallest and the biggest" is a claim, and an interviewer will ask you to justify it.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/maximum-product-of-three-numbers)
