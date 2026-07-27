# 1. Two Sum
> **Easy** &nbsp;·&nbsp; Hash map · complement lookup &nbsp;·&nbsp; family: **Hashing**

The foundational hash-map trade: spend O(n) memory to turn an O(n) search into an O(1) lookup. Note the ordering — check the hash *before* inserting, which is what prevents an element pairing with itself.

**▶ [Step through this solution line by line](../visualizations/0001-two-sum.html)** — 9 steps, traced on `nums = [2,7,11,15], target = 9`.

| | |
|---|---|
| time | O(n) |
| space | O(n) |

## The idea

The complement trick. For each element ask "**what would I need to have already seen?**" and look it up in O(1). This inverts the brute-force question from "search forward for a partner" to "check whether my partner already searched for me", and it is the single most reused idea in array interviews.

## How to recognise it

- "Find two things that combine to X." Sum, difference, product, XOR — the shape is identical, only the arithmetic changes.
- The array is **unsorted** and you may not sort (indices must be preserved). Sorted input would allow the O(1)-space two-pointer version instead.
- You need indices, not values — sorting destroys them, so the hash is the answer.

## Where people go wrong

- **Inserting before looking up.** With `nums = [3,3]`, target 6 you would match index 0 with itself. Look up first, always.
- **Keying by index instead of value.** The dictionary must map *value → index*; the other way round gives you nothing to search by.
- **Assuming exactly one answer when the problem does not say so.** LeetCode guarantees it here; interviewers often remove that guarantee to see whether you noticed.
- **Sorting first.** Tempting, and it works for the two-pointer variant — but sorting scrambles the indices you are asked to return.

## The reusable template

```python
# Complement lookup - look up BEFORE you insert
seen = {}                       # value -> index
for i, x in enumerate(nums):
    if target - x in seen:
        return [seen[target - x], i]
    seen[x] = i

# Same idea on prefix sums (LC 560: count subarrays summing to k)
#   count = {0: 1}; run = 0
#   for x in nums:
#       run += x
#       ans += count.get(run - k, 0)
#       count[run] = count.get(run, 0) + 1
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Input is sorted | LC 167 — converging two pointers, O(1) space, no hash needed. |
| **Three Sum** (LC 15) | Sort, fix one element, two-pointer the rest. O(n²). The sort is affordable because you return values, not indices. |
| Four Sum / k-Sum | Recursive reduction down to two-sum. O(n^(k-1)). |
| Count pairs rather than find one | Same loop, `ans += hash.get(rem, 0)` — count before inserting. |
| **Subarray Sum Equals K** (LC 560) | The same complement trick on *prefix sums*. Recognising that is worth more than either problem alone. |

## How to think about it next time

Whenever you catch yourself writing a nested loop that searches for a partner, stop and ask: **can I precompute what I am searching for into a hash?** That single question converts a large family of O(n²) solutions into O(n). The deeper version — and the one that unlocks LC 560, LC 974 and the whole prefix-sum family — is to ask it about *derived* quantities too: not just "have I seen this value", but "have I seen this running sum, this remainder, this sorted signature".

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/two-sum)
