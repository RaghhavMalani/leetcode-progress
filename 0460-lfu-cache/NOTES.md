# 460. LFU Cache
> **Hard** &nbsp;·&nbsp; Design · three maps + per-frequency LRU lists &nbsp;·&nbsp; family: **Design**

LRU with one more dimension. Evict by lowest frequency, and break ties by recency — which means each frequency needs its own LRU list, plus a running minimum so eviction stays O(1).

**▶ [Step through this solution line by line](../visualizations/0460-lfu-cache.html)** — 40 steps, traced on `capacity = 2, then a sequence of put/get calls`.

| | |
|---|---|
| time | O(1) for get and put |
| space | O(capacity) |

## The idea

Compose structures, one per requirement. **O(1) lookup by key** → hash map. **Evict the least frequent** → group keys by frequency. **Break frequency ties by recency** → each frequency bucket is itself an ordered (LRU) list. **Find the minimum frequency in O(1)** → maintain it incrementally, since it only ever increases by one or resets to 1.

## How to recognise it

- "Evict by usage count", "least frequently used", multi-level cache policies.
- Any ranking with a tie-breaker: the primary key selects a bucket, the secondary key orders within it.
- The `lfuCnt` trick generalises — a running minimum is maintainable in O(1) whenever it changes only in predictable ways.

## Where people go wrong

- **Forgetting `lfuCnt = min(lfuCnt, count[key])` after a put.** A new key has frequency 1; without the reset the eviction bucket is empty and everything breaks. It is the single hardest line to remember.
- **Not removing the evicted key from all three maps.** Any one left behind is a leak or a wrong answer.
- **Advancing `lfuCnt` unconditionally.** It only advances when the old minimum bucket becomes EMPTY — line 53 checks both conditions.
- **Using a heap for the minimum frequency.** O(log n) per operation and stale entries to clean up. The incremental counter is both simpler and faster.
- **Forgetting that `get` counts as a use.** Same trap as LRU.
- **capacity == 0.** Line 63 returns immediately; without it you evict from an empty cache.

## The reusable template

```python
# lookup -> map;  evict-min -> bucket by frequency;
# tie-break -> LRU list inside each bucket;  find-min -> running counter

valMap   = {}                       # key -> value
countMap = defaultdict(int)         # key -> use count
listMap  = defaultdict(LinkedList)  # frequency -> LRU list of keys
lfu      = 0                        # current minimum frequency

def touch(key):                     # called by BOTH get and put
    c = countMap[key]; countMap[key] += 1
    listMap[c].pop(key); listMap[c + 1].push_right(key)
    if c == lfu and listMap[c].empty():
        lfu += 1                    # only when the old min bucket EMPTIES

def put(key, value):
    if cap == 0: return
    if key not in valMap and len(valMap) == cap:
        gone = listMap[lfu].pop_left()          # LFU, ties broken by LRU
        valMap.pop(gone); countMap.pop(gone)    # ALL structures
    valMap[key] = value
    touch(key)
    lfu = min(lfu, countMap[key])   # <- THE line everyone forgets. new key -> 1.
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **LRU Cache** (LC 146) | Drop the frequency dimension entirely — one list. Also in your repo. |
| LFU with ageing | Periodically halve all counts so old hot keys decay. |
| **All O(1) Data Structure** (LC 432) | The same frequency-bucket idea, with buckets in a doubly linked list. |
| Approximate LFU | Sample a few keys and evict the worst — what Redis actually does, because exact LFU costs memory. |

## How to think about it next time

Hard design problems are **layered**, and the way in is to list the required operations and give each one a structure. Write them as a table: lookup → map; evict-min → bucket by key; tie-break → order within bucket; find-min → incremental counter. Then the only remaining work is keeping the layers consistent, which is where every bug lives — so for each mutation, ask explicitly "which of my structures does this touch?" and update all of them in one place.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/lfu-cache)
