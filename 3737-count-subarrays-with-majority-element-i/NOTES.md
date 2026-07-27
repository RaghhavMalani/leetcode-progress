# 3737. Count Subarrays With Majority Element I
> **Medium** &nbsp;·&nbsp; Brute force with incremental state &nbsp;·&nbsp; family: **Brute force done right**

The intended O(n²) solution — but note the one detail that makes it O(n²) and not O(n³): the count is carried forward as `j` advances instead of being recomputed.

**▶ [Step through this solution line by line](../visualizations/3737-count-subarrays-with-majority-element-i.html)** — 26 steps, traced on `nums = [1,2,1,1], target = 1`.

| | |
|---|---|
| time | O(n²) |
| space | O(1) |

## The idea

Even when brute force is the intended answer, structure it so that extending the window is **O(1)**, not O(length). That single discipline is the difference between O(n²) and O(n³), and it is also the seed of every sliding-window and prefix-sum optimisation.

## How to recognise it

- Small constraints (n ≤ 1000ish) explicitly permitting the quadratic answer — and a "Part II" with bigger constraints that does not.
- "Majority" means strictly more than half: `count > length // 2`. Note that with `//` this is correct for both odd and even lengths.
- The reframing that unlocks Part II: map target → +1 and everything else → −1. Then "majority" becomes "the sum of the subarray is positive".

## Where people go wrong

- **Recounting the target inside the inner loop.** O(n³) and it will time out even here.
- **`count >= length / 2`.** Majority is strict, and float division introduces its own problems. Use `count * 2 > length` to avoid both issues.
- **Forgetting to reset `target_count`** when `i` advances.
- **Confusing this with Boyer–Moore majority vote.** That finds the majority of the WHOLE array; here you need per-subarray counts.

## The reusable template

```python
# O(n^2) done right: carry the count, do not recompute it
ans = 0
for i in range(n):
    cnt = 0
    for j in range(i, n):
        cnt += (nums[j] == target)          # O(1) extension
        if cnt * 2 > (j - i + 1):           # strict majority, no float division
            ans += 1
return ans

# for n up to 1e5 (part II): map target -> +1, others -> -1.
# "majority" becomes "prefix[j+1] > prefix[i]", then count inversions
# with a Fenwick tree or merge sort in O(n log n).
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Part II** (LC 3739) | Same question, n up to 10⁵. Use the +1/−1 transform, then count pairs of prefix sums with p[j] > p[i] using a Fenwick tree or merge sort. Also in your repo. |
| **Majority Element** (LC 169) | Boyer–Moore vote, O(n) time and O(1) space. |
| Count subarrays with sum > 0 | Exactly what the transform reduces this to. |
| Count subarrays with sum equal to k | LC 560 — prefix sums plus a hash map. |

## How to think about it next time

Two lessons. First: **make brute force incremental** — carrying state as the window grows is free and usually saves a whole factor of n. Second, and more valuable: learn the **+1/−1 transform**. "More X than Y in this range" becomes "positive sum in this range", which converts a counting problem into a prefix-sum problem and opens the door to hash maps, BITs and merge sort. That transform is the entire content of Part II, and it recurs constantly.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/count-subarrays-with-majority-element-i)
