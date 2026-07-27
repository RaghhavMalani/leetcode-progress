# 706. Design HashMap
> **Easy** &nbsp;·&nbsp; Design · hash table internals &nbsp;·&nbsp; family: **Design**

LC 705 with values attached. The detail worth arguing about is the `-1` sentinel for a missing key — a design smell that a real API would handle differently.

**▶ [Step through this solution line by line](../visualizations/0706-design-hashmap.html)** — 10 steps, traced on `put(1,1), put(2,2), get(1), get(3), put(2,1), get(2), remove(2), get(2)`.

| | |
|---|---|
| time | O(1) average, O(n) worst case if every key collides |
| space | O(n) |

## The idea

Same buckets as a hash set, but each bucket stores `(key, value)` pairs. On `put` you scan the chain: found → overwrite, not found → append. That "overwrite or append" is the only structural difference from a set.

## How to recognise it

- Any "implement a dictionary/cache/index without the built-in".
- It is also the base layer of almost every design question — LRU, LFU, insert-delete-getRandom, time-based key-value store all begin "a hash map, plus…".

## Where people go wrong

- **The `-1` sentinel.** Fine because the problem promises values are non-negative — but say that out loud. A real API returns `None`, raises, or takes a default, because otherwise you cannot store −1.
- **Appending on `put` without checking for the key.** Duplicate entries in the chain, and `get` may return a stale value.
- **Forgetting the `if key in` guard on remove.** `del` on a missing key raises KeyError.
- **Never resizing.** Fixed bucket counts degrade to linear scans at scale.

## The reusable template

```python
# Buckets of (key, value) pairs
class MyHashMap:
    def __init__(self):
        self.n = 1000
        self.buckets = [[] for _ in range(self.n)]

    def put(self, key, value):
        b = self.buckets[hash(key) % self.n]
        for i, (k, _) in enumerate(b):
            if k == key:
                b[i] = (key, value)       # OVERWRITE, do not append
                return
        b.append((key, value))

    def get(self, key):
        for k, v in self.buckets[hash(key) % self.n]:
            if k == key:
                return v
        return -1                          # sentinel - a real API returns None
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **LRU Cache** (LC 146) | Hash map + doubly linked list for O(1) eviction. In your repo. |
| **LFU Cache** (LC 460) | Hash map + a map from frequency to a list. Also in your repo, and considerably harder. |
| **Insert Delete GetRandom O(1)** (LC 380) | Hash map of value→index, plus an array. Delete by swapping with the last element. |
| **Time-Based Key-Value Store** (LC 981) | Map of key → sorted list of (timestamp, value), then binary search. |

## How to think about it next time

Notice how many "hard" design problems are **a hash map composed with one other structure**. Map + doubly linked list = LRU. Map + array = O(1) random removal. Map + heap = a priority index. Map + sorted list = time queries. When a design question lands, start by writing "hash map for O(1) lookup by key" and then ask what the *other* required operation needs — that second structure is the actual answer.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/design-hashmap)
