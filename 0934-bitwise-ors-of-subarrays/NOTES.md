# 934. Bitwise ORs of Subarrays
> **Medium** &nbsp;&middot;&nbsp; Monotone bit operation · bounded frontier &nbsp;&middot;&nbsp; family: **Bit manipulation**

The complement of LC 2503 in your repo. There, AND only clears bits so runs matter. Here, OR only sets bits — which bounds the set of distinct values ending at each index to about 30.

**▶ [Step through this solution line by line](./visualization.html)** — 14 steps, traced on `arr = [1,2,4]`.

| | |
|---|---|
| time | O(n · 32) |
| space | O(n · 32) for the result set |

## The idea

Fix the right endpoint at i and consider all subarrays ending there. As you extend leftwards the OR is **non-decreasing and can only gain bits**, so it takes at most 32 distinct values. Carrying that small frontier from index to index turns an O(n²) enumeration into O(32n).

## How to recognise it

- OR / AND / GCD over all subarrays. All three are monotone under extension, and all three admit exactly this "small set of values ending here" trick.
- GCD is the other big one: extending a subarray can only divide the GCD down, so it changes at most log(max) times.
- If the operation is a plain sum, this does NOT apply — sums take n distinct values, and you need prefix sums instead.

## Where people go wrong

- **Forgetting to add the single-element subarray.** Line 11. On the first iteration `current_ors` is empty, so without it nothing is ever produced.
- **Using a list instead of a set.** The bound depends entirely on duplicates collapsing; a list grows to O(n) and you are back to O(n²).
- **Reusing the same set object** instead of building a fresh `next_ors`. Mutating while iterating gives wrong answers.
- **Assuming the O(n²) solution passes.** With n up to 5×10⁴ it does not.

## The reusable template

```python
# carry the set of ORs of subarrays ENDING at i - it stays tiny (<= 32)
result, cur = set(), set()
for x in arr:
    cur = {x | y for y in cur} | {x}    # extend all, plus the singleton
    result |= cur
return len(result)

# same trick works for GCD (bounded by log(max)) and AND.
# NOT for sums - those take O(n) distinct values, use prefix sums.
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Longest Subarray With Maximum AND** (LC 2503) | AND only clears bits, so the max AND is max(nums) and you just find the longest run. Also in your repo. |
| Distinct GCDs of all subarrays | Same frontier trick, GCD instead of OR, bounded by log(max). |
| Count subarrays with OR ≥ k | Same frontier, and each entry also carries how many subarrays produce it. |
| Subarray SUMS | Prefix sums plus a hash map — a completely different technique. |

## How to think about it next time

The generalisable question is: **"as I extend a subarray, how many distinct values can this aggregate take?"** For OR and AND it is bounded by the bit width; for GCD by log of the maximum; for min and max by the number of distinct elements; for sum it is unbounded. When that count is small, you can carry the whole frontier and get a near-linear algorithm for free. That single question turns several intimidating "all subarrays" problems into short loops.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/bitwise-ors-of-subarrays)
