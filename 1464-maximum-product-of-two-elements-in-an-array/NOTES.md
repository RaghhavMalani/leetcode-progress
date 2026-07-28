# 1464. Maximum Product of Two Elements in an Array
> **Easy** &nbsp;&middot;&nbsp; Single pass · top-k tracking &nbsp;&middot;&nbsp; family: **Math & number theory**

Track the top two in one pass, no sort. The detail that matters is the demotion order — `max2 = max1` must happen before `max1 = num`.

**▶ [Step through this solution line by line](./visualization.html)** — 13 steps, traced on `nums = [3,4,5,2]`.

| | |
|---|---|
| time | O(n) — beats the O(n log n) sort |
| space | O(1) |

## The idea

For a small fixed k, tracking the top k in one pass is strictly better than sorting. The pattern is a cascade: a new value that beats first place shifts everyone down; one that beats only second place inserts there. It generalises to k slots, though beyond k ≈ 3 a size-k heap is cleaner.

## How to recognise it

- "Largest two / smallest three / top k" where k is a tiny constant.
- The instinct to sort — check whether you actually need the whole order or just the extremes.
- For larger k over a stream, this becomes a bounded heap (LC 703, in your repo).

## Where people go wrong

- **Assigning `max1` before demoting it.** Then max2 gets the new value too and you square one element.
- **Using two `if`s instead of `if/elif`.** Same failure by a different route.
- **Initialising both to 0.** Safe here because the constraints promise values ≥ 1; with negatives allowed you would need −∞.
- **Forgetting the −1 in the formula.** The problem asks for (nums[i]−1)×(nums[j]−1), not the raw product.

## The reusable template

```python
# track the top two in one pass - order of assignment matters
max1 = max2 = float('-inf')          # 0 only if values are guaranteed >= 0
for x in nums:
    if x > max1:
        max2 = max1                  # DEMOTE first...
        max1 = x                     # ...then promote
    elif x > max2:                   # elif, not a second if
        max2 = x
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Three numbers, negatives allowed | LC 628 — sorting plus case analysis. Also in your repo. |
| Top k over a stream | LC 703 — a size-k min-heap. |
| Second largest DISTINCT value | Add an equality guard so duplicates do not fill both slots. |
| Largest and smallest together | Four running variables, one pass. |

## How to think about it next time

Before writing `sort()`, ask **"how much of the order do I actually need?"** If the answer is "the top two", a single pass gives it in O(n). This shows up constantly — max and min (LC 3689 in your repo), the two largest, the k most frequent (LC 347, where buckets beat both). Sorting is the default answer that is very often one complexity class too slow.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array)
