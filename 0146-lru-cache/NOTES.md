# 146. LRU Cache
> **Medium** &nbsp;·&nbsp; Design · hash map + doubly linked list &nbsp;·&nbsp; family: **Hashing**

The archetypal composition question. A hash map alone cannot track recency; a linked list alone cannot look up in O(1). Together they do both — and the two sentinel nodes remove every edge case.

**▶ [Step through this solution line by line](../visualizations/0146-lru-cache.html)** — 31 steps, traced on `capacity = 2, then put/get operations`.

| | |
|---|---|
| time | O(1) for both get and put |
| space | O(capacity) |

## The idea

Two requirements pull in different directions. **O(1) lookup by key** needs a hash map. **O(1) "move to most recent" and O(1) "evict the oldest"** need a doubly linked list, because unlinking a node you already have a pointer to is four assignments. The map stores *node references*, which is the bridge between them.

## How to recognise it

- "Design a cache", "evict the least recently used", "O(1) for all operations".
- Generally: whenever you need both key-lookup AND ordering, the answer is a map plus an ordered structure, with the map storing handles into it.
- The follow-up "why not a singly linked list?" has a specific answer — you would need the predecessor to unlink, which costs O(n) to find.

## Where people go wrong

- **Deleting from the list but not the map** (or vice versa). The two must stay in lockstep. This is the bug that passes small tests and fails at scale.
- **No sentinels.** Then insert/delete need null checks at both ends and the code triples in length. Two dummy nodes cost nothing.
- **Forgetting that `get` counts as a use.** A read must move the node to the MRU end, not just return the value.
- **In `put`, not deleting the old node when the key already exists.** You get two nodes for one key and the eviction order goes wrong.
- **Using `OrderedDict`.** `move_to_end` and `popitem(last=False)` solve this in ten lines — a great answer to give *after* showing you can build it, never instead.

## The reusable template

```python
# hash map (key -> NODE) + doubly linked list with two sentinels
class LRUCache:
    def __init__(self, cap):
        self.cap, self.cache = cap, {}
        self.lru, self.mru = Node(0,0), Node(0,0)      # sentinels
        self.lru.next, self.mru.prev = self.mru, self.lru

    def _remove(self, n):                  # 4 assignments, no null checks
        n.prev.next, n.next.prev = n.next, n.prev

    def _insert(self, n):                  # attach at the MRU end
        p = self.mru.prev
        p.next = n; self.mru.prev = n
        n.prev = p;  n.next = self.mru

    def get(self, key):
        if key not in self.cache: return -1
        n = self.cache[key]
        self._remove(n); self._insert(n)   # a READ counts as a use
        return n.value

    def put(self, key, value):
        if key in self.cache: self._remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.lru.next
            self._remove(lru)
            del self.cache[lru.key]        # BOTH structures. always.
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **LFU Cache** (LC 460) | Evict by frequency, tie-broken by recency. Needs a map of frequency → list. Also in your repo, and genuinely harder. |
| TTL / expiring cache | Add a heap or a timing wheel keyed by expiry. |
| **All O(1) Data Structure** (LC 432) | The same map + doubly-linked-list-of-buckets idea, escalated. |
| Thread-safe LRU | A lock, or sharding by key hash. The right thing to raise in a systems interview. |

## How to think about it next time

Whenever a design problem demands O(1) for two operations that seem to conflict, the answer is almost always **two structures, cross-referenced**. Write the two requirements in a column, pick the structure that makes each one O(1), then ask what pointer has to connect them. Here: map → node. In LC 380 it is map → array index. In LFU it is map → node plus frequency → list. Once you see that shape, these problems stop being memorisation.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/lru-cache)
