# 23. Merge k Sorted Lists
> **Hard** &nbsp;·&nbsp; Divide and conquer · pairwise merge &nbsp;·&nbsp; family: **Sorting & divide and conquer**

Merging pairwise in rounds instead of one-at-a-time into an accumulator. Same total merges, but each element is copied log k times instead of k times — O(N log k) rather than O(N k).

**▶ [Step through this solution line by line](../visualizations/0023-merge-k-sorted-lists.html)** — 31 steps, traced on `lists = [[1,4,5],[1,3,4],[2,6]]`.

| | |
|---|---|
| time | O(N log k) — N total nodes, log k rounds |
| space | O(1) extra (plus O(k) for the list array) |

## The idea

The naive "merge list 1 into the accumulator, then list 2, then list 3…" is O(Nk), because the elements of the first list get re-copied in every single merge. **Pairwise merging** makes every element participate in exactly log k merges. This is the same reasoning that makes merge sort O(n log n) rather than O(n²).

## How to recognise it

- "Merge k sorted X" — lists, arrays, streams, files.
- k-way problems generally: think either **divide and conquer** (this) or a **size-k heap** (the other O(N log k) answer).
- The heap version is better when the lists arrive as a stream or k is huge; this version is better when you have them all up front and want O(1) extra space.

## Where people go wrong

- **Sequential merging.** Correct, and it is what most people write first. Be able to explain why it is O(Nk) and this is O(N log k).
- **Not handling an odd count.** `lists[i+1] if i+1 < len(lists) else None` — the last list pairs with None and passes through.
- **`while len(lists) > 1`, not `>= 1`.** The latter loops forever.
- **Empty input.** `lists = []` makes `lists[0]` throw — hence the guard on line 8.
- **The heap version needs a tiebreaker.** `(node.val, i, node)` — without the index, Python tries to compare ListNodes when values tie and raises.

## The reusable template

```python
# Pairwise merge in rounds - O(N log k), not O(N k)
while len(lists) > 1:
    merged = []
    for i in range(0, len(lists), 2):
        a = lists[i]
        b = lists[i + 1] if i + 1 < len(lists) else None   # odd count -> None
        merged.append(merge_two(a, b))
    lists = merged                    # count HALVES every round
return lists[0]

# heap alternative, also O(N log k), better for streams:
#   h = [(node.val, i, node) for i, node in enumerate(heads) if node]
#   ...pop the smallest, push its successor.  the `i` is a tiebreaker so
#   Python never has to compare two ListNodes.
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Heap version | Push the head of every list, pop the smallest, push its successor. O(N log k), O(k) space, and the natural answer for streams. |
| Merge k sorted **arrays** | Same two strategies; with arrays you can also concatenate and sort for O(N log N), which is worse but simpler. |
| **Sort List** (LC 148) | Merge sort a single list — split with fast/slow, then this same merge. |
| **Smallest range covering k lists** (LC 632) | Heap plus a sliding window over the k current heads. |

## How to think about it next time

When you have k things to combine, always ask: **can I combine them in a tree instead of a chain?** Chain = O(Nk), tree = O(N log k), and the code is barely longer. The same insight applies to concatenating k strings, unioning k sets, and multiplying k matrices. Whenever your algorithm repeatedly touches the same data because it sits in the accumulator, restructure the combination order.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/merge-k-sorted-lists)
