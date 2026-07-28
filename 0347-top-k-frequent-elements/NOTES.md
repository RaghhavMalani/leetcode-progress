# 347. Top K Frequent Elements
> **Medium** &nbsp;&middot;&nbsp; Bucket sort · frequency &nbsp;&middot;&nbsp; family: **Hashing**

The O(n) answer that beats both sorting and the heap. It works because a frequency is bounded by n, which means you can use it directly as an array index.

**▶ [Step through this solution line by line](./visualization.html)** — 18 steps, traced on `nums = [1,1,1,2,2,3], k = 2`.

| | |
|---|---|
| time | O(n) — beats heap O(n log k) and sort O(n log n) |
| space | O(n) |

## The idea

**Bucket sort by an index-able key.** Whenever the value you would sort by is a bounded non-negative integer, you can skip sorting entirely: make an array indexed by that value and drop items into it. Here the key is frequency, bounded by n, so n+1 buckets always suffice.

## How to recognise it

- "Top k", "k most frequent", "k largest" — and then check whether the sort key is a small bounded integer. If yes, bucket. If not, heap.
- Frequencies, ages, scores out of 100, character counts — all bounded, all bucketable.
- If k is close to n, bucketing wins outright; if k is tiny and n is huge, a size-k heap uses less memory.

## Where people go wrong

- **Sizing the buckets as `len(freq)`.** The index is a *frequency*, whose maximum is `len(nums)`, not the number of distinct values. Get this wrong and you index out of range on `[1,1,1]`.
- **Looping `range(len(buckets)-1, 0, -1)` vs `-1`.** Bucket 0 is always empty (a number present in the list appears at least once) so stopping at 1 is right — but be able to say why.
- **Forgetting to stop at k.** Without the early return you can return more than k elements when several tie.
- **Reaching for `heapq.nlargest` first.** Fine as a first answer, but the interviewer asking "can you do better than O(n log k)?" is asking for exactly this.

## The reusable template

```python
# Bucket by a bounded integer key - counting sort in disguise
freq = Counter(nums)
buckets = [[] for _ in range(len(nums) + 1)]   # size = MAX POSSIBLE KEY + 1
for num, c in freq.items():
    buckets[c].append(num)

res = []
for c in range(len(buckets) - 1, 0, -1):       # read from the top down
    for num in buckets[c]:
        res.append(num)
        if len(res) == k:
            return res
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| k closest points to the origin | LC 973 — distances are unbounded, so heap or quickselect, not buckets. |
| **Kth largest element** (LC 215) | Quickselect for O(n) average, heap for O(n log k) worst case. |
| Sort characters by frequency | LC 451 — same buckets, emit all of them instead of stopping at k. |
| Streaming top-k | Buckets do not work; keep a size-k min-heap. |

## How to think about it next time

Add one question to your checklist whenever you are about to sort: **"is my sort key a bounded small integer?"** If it is, you can index by it and drop from O(n log n) to O(n). This is the same realisation behind counting sort, radix sort, and the bucket trick in LC 164. It costs nothing to check and occasionally hands you a whole complexity class.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/top-k-frequent-elements)
