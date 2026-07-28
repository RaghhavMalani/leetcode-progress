# 622. Design Circular Queue
> **Medium** &nbsp;&middot;&nbsp; Design · doubly linked list with sentinels &nbsp;&middot;&nbsp; family: **Linked lists**

Your solution uses a doubly linked list with two sentinels and a free-space counter. The classic alternative — a fixed array with modular indices — is where the name "circular" actually comes from.

**▶ [Step through this solution line by line](./visualization.html)** — 18 steps, traced on `k = 3, then enQueue/deQueue/Front/Rear/isFull operations`.

| | |
|---|---|
| time | O(1) for every operation |
| space | O(k) |

## The idea

A bounded FIFO. Two implementations, both O(1): a **doubly linked list with sentinels** (this one — allocation per element, but no index arithmetic) or a **fixed array with head/tail indices mod k** (no allocation, better cache behaviour, but you must resolve the full-vs-empty ambiguity). Knowing both and being able to compare them is the point of the question.

## How to recognise it

- "Design a queue/buffer with fixed capacity" — ring buffers, producer/consumer, sliding windows over streams.
- The `Rear()` requirement is what forces a DOUBLY linked list; without it a singly linked list with a tail pointer suffices.
- Real systems use ring buffers everywhere: audio, networking, logging.

## Where people go wrong

- **The array version’s full-vs-empty ambiguity.** With only head and tail, `head == tail` means both. Fix it by keeping a size counter (as this solution does with `space`) or by leaving one slot permanently unused.
- **Computing size by walking the list.** O(n) where a counter is O(1).
- **Forgetting to update BOTH directions** when splicing a node into a doubly linked list. Four assignments, every time.
- **Not returning the required booleans / −1 sentinels.** The API contract is part of the problem.

## The reusable template

```python
# the OTHER implementation - fixed array + modular indices (a real ring buffer)
class MyCircularQueue:
    def __init__(self, k):
        self.a, self.k = [0] * k, k
        self.head = self.size = 0

    def enQueue(self, v):
        if self.size == self.k: return False
        self.a[(self.head + self.size) % self.k] = v      # wrap with %
        self.size += 1
        return True

    def deQueue(self):
        if self.size == 0: return False
        self.head = (self.head + 1) % self.k
        self.size -= 1
        return True

    def Front(self): return -1 if not self.size else self.a[self.head]
    def Rear(self):  return -1 if not self.size else self.a[(self.head + self.size - 1) % self.k]

# the `size` counter resolves the head==tail full-vs-empty ambiguity.
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Design Circular Deque** (LC 641) | Insert and delete at both ends — the doubly linked list version barely changes. |
| **LRU Cache** (LC 146) | Same sentinel-bracketed doubly linked list, plus a hash map. Also in your repo. |
| Growable ring buffer | On overflow, allocate double and copy — amortised O(1). |
| Lock-free ring buffer | Single producer / single consumer with atomic indices — the systems-interview version. |

## How to think about it next time

For design questions, decide the **representation** first and the code follows. Array + modular indices: contiguous memory, no allocation, index arithmetic to get right. Linked list + sentinels: no arithmetic, no resizing, one allocation per element. Neither is universally better — say the trade-off out loud and pick deliberately. That sentence is what is actually being graded.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/design-circular-queue)
