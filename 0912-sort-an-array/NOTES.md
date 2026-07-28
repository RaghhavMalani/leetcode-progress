# 912. Sort an Array
> **Medium** &nbsp;&middot;&nbsp; Divide and conquer · merge sort &nbsp;&middot;&nbsp; family: **Sorting & divide and conquer**

Merge sort from scratch. Watch the recursion tree: depth log n, O(n) work per level. That picture *is* the complexity proof, and it transfers to every divide-and-conquer algorithm.

**▶ [Step through this solution line by line](./visualization.html)** — 36 steps, traced on `nums = [5,2,3,1]`.

| | |
|---|---|
| time | O(n log n) always — best, average and worst |
| space | O(n) for the merge buffers, O(log n) for the stack |

## The idea

**Divide and conquer:** split into halves, solve each recursively, combine. The recurrence T(n) = 2T(n/2) + O(n) resolves to O(n log n) — log n levels, O(n) merging per level. Merge sort’s distinguishing features are that it is **stable** and has **no bad case**, which is why it is what Python’s Timsort is built on.

## How to recognise it

- The problem explicitly forbids built-in sort, or the follow-up asks for a guaranteed O(n log n).
- The merge step is reusable on its own — it is exactly LC 21 and LC 23 in your repo.
- Counting inversions, counting smaller elements to the right (LC 315), and count-of-range-sums (LC 327) are all merge sort with bookkeeping added to the merge.

## Where people go wrong

- **`left[i] < right[j]` instead of `<=`.** Breaks stability. Irrelevant for bare integers, fatal when elements carry payloads.
- **Forgetting the drain loops.** When one half runs out the other still has elements — losing them silently truncates the output.
- **Slicing at every level.** `arr[:mid]` allocates, giving O(n log n) total allocation. Passing indices into a shared buffer is the production version.
- **Choosing quicksort for this problem.** LeetCode’s test data includes adversarial cases that make naive quicksort O(n²). Merge sort or heapsort is the safe answer.

## The reusable template

```python
def mergesort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    return merge(mergesort(a[:mid]), mergesort(a[mid:]))

def merge(L, R):
    res, i, j = [], 0, 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:          # <= keeps the sort STABLE
            res.append(L[i]); i += 1
        else:
            res.append(R[j]); j += 1
    res += L[i:]                  # drain BOTH remainders
    res += R[j:]
    return res

# T(n) = 2T(n/2) + O(n)  ->  O(n log n).  log n levels, O(n) work per level.
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Sort List** (LC 148) | Merge sort on a linked list — split with fast/slow, and the merge is O(1) space. |
| **Count inversions** / **Count of Smaller Numbers After Self** (LC 315) | Count cross-pairs during the merge. |
| Quicksort | O(n log n) average, O(1) extra space, but O(n²) adversarial. Randomise the pivot. |
| Heapsort | O(n log n) worst case AND O(1) space, but not stable and cache-unfriendly. |
| Bounded integer keys | Counting or radix sort — O(n). See LC 347 and LC 1833 in your repo. |

## How to think about it next time

Know your sorting algorithms by their **trade-off profile**, not their code: merge = stable + guaranteed + O(n) space; quick = in place + fast in practice + bad worst case; heap = guaranteed + in place + unstable; counting/radix = linear but only for bounded keys. Interviewers rarely want you to write one — they want you to pick the right one and say why. And internalise the recursion-tree picture: "log n levels × O(n) per level" is how you will reason about complexity for every divide-and-conquer algorithm you meet.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/sort-an-array)
