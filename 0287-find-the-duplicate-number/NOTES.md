# 287. Find the Duplicate Number
> **Medium** &nbsp;·&nbsp; Floyd cycle detection · fast & slow &nbsp;·&nbsp; family: **Two pointers & sliding window**

The famous disguise: an array of integers is secretly a linked list, and finding a duplicate value is secretly finding where a cycle begins. Two phases — detect, then locate.

**▶ [Step through this solution line by line](../visualizations/0287-find-the-duplicate-number.html)** — 22 steps, traced on `nums = [1,3,4,2,2]`.

| | |
|---|---|
| time | O(n) |
| space | O(1) — the constraint that rules out a set, and the reason this problem is famous |

## The idea

Two ideas stacked. **(1) Reframing:** reading `i → nums[i]` turns the array into a functional graph; n+1 nodes with values in 1..n forces a cycle whose entrance is the repeated value. **(2) Floyd:** a fast pointer and a slow pointer must meet inside a cycle; then resetting one to the head and advancing both at the same speed makes them meet exactly at the entrance.

## How to recognise it

- The pair of constraints "**do not modify the array**" and "**O(1) extra space**". Together they eliminate sorting, a set, and marking-by-negation — which is the interviewer pointing at Floyd.
- n+1 numbers in the range 1..n — a pigeonhole setup, and it also guarantees index 0 is never a cycle member, so starting there is safe.
- Any "find the start of the cycle" phrasing, in a list or in a functional graph.

## Where people go wrong

- **Returning the meeting point from phase one.** The most common error. That index is somewhere in the cycle, not necessarily its entrance.
- **Starting `fast` at `nums[0]` instead of 0**, or otherwise mismatching the two phases’ starting offsets. Both pointers must start at the same node.
- **Using a `while slow != fast` loop that never runs** because both start at 0. That is why the code is `while True` with the check at the bottom.
- **Forgetting why a cycle is guaranteed** — if asked and you cannot say "pigeonhole", the elegance reads as memorisation.

## The reusable template

```python
# Floyd's cycle detection - two phases, never one
# phase 1: find A meeting point (proves a cycle exists)
slow = fast = start
while True:
    slow = nxt(slow)
    fast = nxt(nxt(fast))
    if slow == fast:
        break

# phase 2: reset one pointer to the start, step BOTH one at a time.
# they meet exactly at the cycle entrance.
slow2 = start
while slow != slow2:
    slow  = nxt(slow)
    slow2 = nxt(slow2)
return slow
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Linked List Cycle** (LC 141) | Phase one only — you just need a yes/no. |
| **Linked List Cycle II** (LC 142) | Literally this algorithm on an actual list. Same two phases. |
| Modification allowed | Mark visited by negating `nums[abs(x)]` — O(n) time, O(1) space, far easier to derive. |
| Extra space allowed | A set, or counting sort. Say this first; it shows you know the constraint is what makes it hard. |
| Find **all** duplicates | LC 442 — the index-negation trick, since Floyd only finds one. |

## How to think about it next time

The transferable skill is **reframing**. Before reaching for an algorithm, ask what structure the data secretly has. "Array of indices" → functional graph. "Pairs that must match" → graph edges. "Prefix sums" → a line you can binary search. Most Hard problems are a Medium problem wearing a disguise, and the interview is testing whether you can undress it. Practise by asking, of every array problem: *if I read this as a graph, what are the nodes and edges?*

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/find-the-duplicate-number)
