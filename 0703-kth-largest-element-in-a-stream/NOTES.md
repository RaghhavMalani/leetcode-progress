# 703. Kth Largest Element in a Stream
> **Easy** &nbsp;&middot;&nbsp; Heap · bounded size-k min-heap &nbsp;&middot;&nbsp; family: **Sorting & divide and conquer**

The inversion worth memorising: **k largest → min-heap of size k**. The root is the weakest survivor, which is exactly the kth largest, and it makes eviction O(1) to find.

**▶ [Step through this solution line by line](./visualization.html)** — 25 steps, traced on `k = 3, nums = [4,5,8,2], then add(3), add(5), add(10), add(9), add(4)`.

| | |
|---|---|
| time | O(n) to build, O(log k) per add |
| space | O(k) — independent of stream length |

## The idea

Keep only what can still matter. If you only ever need the kth largest, anything outside the top k is dead weight. A min-heap of size k keeps exactly the survivors, and its root — the smallest survivor — is the answer. Every new value is compared against that root in O(1) and either replaces it or is discarded.

## How to recognise it

- "Kth largest / smallest", especially over a **stream** where you cannot hold everything.
- "Top k" anything: k closest points, k most frequent (though LC 347 in your repo has a better O(n) bucket answer), k pairs with smallest sums.
- The size bound is what to look for — if the answer only depends on k items, do not store n.

## Where people go wrong

- **Using a max-heap.** Intuitive and wrong: a max-heap of size k would evict the *largest*, which is the thing you most want to keep.
- **Sorting on every add.** O(n log n) per call instead of O(log k).
- **Pushing before checking the size, or after — it matters for the edge cases.** Push then pop if oversized is the clean order and handles the initial fill for free.
- **Assuming the initial list has at least k elements.** It might not; the heap simply fills up as adds arrive, and this code handles that correctly.

## The reusable template

```python
# k LARGEST -> min-heap of size k.  (k smallest -> max-heap, negate values)
import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.h = nums
        heapq.heapify(self.h)               # O(n), better than n pushes
        while len(self.h) > k:
            heapq.heappop(self.h)

    def add(self, val):
        heapq.heappush(self.h, val)         # push first...
        if len(self.h) > self.k:
            heapq.heappop(self.h)           # ...then trim
        return self.h[0]                    # root = kth largest
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Kth Largest Element in an Array** (LC 215) | Quickselect for O(n) average; the heap gives O(n log k). |
| **Top K Frequent** (LC 347) | Bucket sort beats the heap here — O(n). Your repo uses the better one. |
| **Median from a data stream** (LC 295) | Two heaps, a max-heap for the low half and a min-heap for the high half. |
| **Merge k sorted lists** (LC 23) | A size-k heap of list heads. Your repo uses divide-and-conquer instead. |
| Sliding window maximum | LC 239 — a monotonic deque, not a heap, because you must evict by position not by value. |

## How to think about it next time

The reusable question is **"what is the smallest set of items that could still affect the answer?"** If it is bounded by k, use a size-k heap and throw the rest away as it arrives. This is the core idea behind streaming algorithms in general, and it is why "the input does not fit in memory" is usually not fatal. The direction inversion — min-heap for max-k — trips up almost everyone once; get it wrong deliberately on paper today and you will never get it wrong again.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/kth-largest-element-in-a-stream)
