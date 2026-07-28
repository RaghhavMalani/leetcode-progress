# 217. Contains Duplicate
> **Easy** &nbsp;&middot;&nbsp; Hash set · membership &nbsp;&middot;&nbsp; family: **Hashing**

Two lines, and worth a minute of thought: the set does the comparing, and the size difference does the reporting. Also worth knowing when this is *not* the best answer.

**▶ [Step through this solution line by line](./visualization.html)** — 6 steps, traced on `nums = [1,2,3,1]`.

| | |
|---|---|
| time | O(n) |
| space | O(n) — the trade being made |

## The idea

A set answers "have I seen this?" in O(1). Almost every duplicate/uniqueness question reduces to that one operation, and the only real decision is whether you can afford the O(n) memory.

## How to recognise it

- "Any duplicates", "all unique", "seen before" with no constraint on space.
- If the problem adds "within k indices" it becomes a sliding window (LC 219). If it adds "O(1) space, do not modify" it becomes Floyd (LC 287). Same question, three completely different answers depending on the constraints — read them first.

## Where people go wrong

- **Building the set when you could exit early.** The explicit loop with `if x in seen: return True` stops at the first duplicate; `set(nums)` always consumes the whole list. Identical big-O, different real-world behaviour on a huge array whose duplicate is at index 2.
- **Offering the O(n²) double loop.** It passes small tests and times out on the real ones.
- **Sorting first.** O(n log n) but O(1) extra space if sorting in place — a legitimate answer when memory is the binding constraint. Knowing when to prefer it is the actual skill.

## The reusable template

```python
# Membership in O(1)
return len(set(nums)) != len(nums)          # shortest

seen = set()                                 # early-exit version
for x in nums:
    if x in seen:
        return True
    seen.add(x)
return False
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Duplicates within k indices | LC 219 — fixed-size sliding window. |
| n+1 values in 1..n, O(1) space, no modification | LC 287 — Floyd cycle detection. |
| Find **all** duplicates in O(1) space | LC 442 — negate `nums[abs(x)-1]` as a visited marker. |
| Streaming / unbounded input | A Bloom filter if false positives are tolerable; otherwise you genuinely need the memory. |

## How to think about it next time

Get in the habit of asking, for every easy problem, **"which constraint would make my answer wrong?"** Here: remove the memory allowance and the set dies; forbid modification too and you need Floyd. Problems 217, 219 and 287 in your repo are the same question under three constraint sets, and seeing them as a family is worth more than solving each in isolation.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/contains-duplicate)
