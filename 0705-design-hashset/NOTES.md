# 705. Design HashSet
> **Easy** &nbsp;&middot;&nbsp; Design · hash table internals &nbsp;&middot;&nbsp; family: **Design**

Your solution wraps a dict, which passes. The interesting version is the one the problem is actually asking for — buckets, a hash function, and a collision strategy — so that is what the theory below covers.

**▶ [Step through this solution line by line](./visualization.html)** — 9 steps, traced on `add(1), add(2), contains(1), contains(3), add(2), remove(2), contains(2)`.

| | |
|---|---|
| time | O(1) average per operation |
| space | O(n) — but this version never shrinks, because remove tombstones |

## The idea

A hash set is an **array of buckets** plus a hash function. `index = hash(key) % num_buckets` tells you which bucket; the bucket holds every key that landed there, and you scan it linearly. Everything else — load factor, resizing, open addressing — is engineering around keeping those buckets short.

## How to recognise it

- "Design / implement X without using the built-in" — the point is the internals, not the API.
- Real interviews ask the follow-ups: what happens on a collision, when do you resize, what is the amortised cost of a resize.

## Where people go wrong

- **Tombstoning instead of deleting** (what this code does). Memory grows without bound under an add/remove-heavy workload. `del self.hashset[key]` is the fix, or `discard` semantics.
- **Ignoring collisions** in a hand-rolled version. Two keys with the same bucket index must both survive — chaining (a list per bucket) is the easy answer.
- **A fixed bucket count.** With 1000 buckets and 10⁶ keys every lookup becomes a 1000-element scan. Resize when load factor exceeds ~0.75.
- **Negative keys with `%`.** In Python `-5 % 10 == 5`, so you are fine; in Java/C++ you are not.

## The reusable template

```python
# What the problem is actually asking for: buckets + chaining
class MyHashSet:
    def __init__(self):
        self.n = 1000
        self.buckets = [[] for _ in range(self.n)]

    def _idx(self, key):
        return hash(key) % self.n

    def add(self, key):
        b = self.buckets[self._idx(key)]
        if key not in b:            # scan the chain
            b.append(key)

    def remove(self, key):
        b = self.buckets[self._idx(key)]
        if key in b:
            b.remove(key)           # ACTUALLY remove - no tombstones

    def contains(self, key):
        return key in self.buckets[self._idx(key)]

# production version also: resize when len/n > 0.75, rehashing everything.
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Design HashMap** (LC 706) | Store (key, value) pairs in the buckets instead of bare keys. |
| Open addressing instead of chaining | On collision, probe the next slot. Better cache behaviour, deletion needs real tombstones. |
| **LRU Cache** (LC 146) | Hash map + doubly linked list — the classic composition. Also in your repo. |
| Bloom filter | O(1) space per element, false positives allowed. The right answer for "is this URL probably in the set of a billion?". |

## How to think about it next time

Design questions are graded on the **trade-offs you volunteer**, not on whether the code runs. For any structure you build, be ready to say: what is the average cost, what is the worst case, what triggers the worst case, and what does it cost in memory. For a hash table the answers are O(1) / O(n) / everything colliding / O(n) with a load factor you choose. Saying those four things unprompted is worth more than a perfect implementation.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/design-hashset)
