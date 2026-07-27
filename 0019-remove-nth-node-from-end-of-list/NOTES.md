# 19. Remove Nth Node From End of List
> **Medium** &nbsp;·&nbsp; Linked list · two pointers with a gap &nbsp;·&nbsp; family: **Two pointers & sliding window**

"From the end" in a singly linked list, in one pass. The trick is a fixed gap: give one pointer an n-step head start and they stay n apart forever.

**▶ [Step through this solution line by line](../visualizations/0019-remove-nth-node-from-end-of-list.html)** — 11 steps, traced on `head = [1,2,3,4,5], n = 2`.

| | |
|---|---|
| time | O(n) — one pass |
| space | O(1) |

## The idea

You cannot walk backwards in a singly linked list, so "the nth from the end" seems to need the length. The **fixed-gap two pointers** trick converts a measurement from the end into a measurement from the start: separate two pointers by n, then move them together until the leading one hits the end.

## How to recognise it

- "nth from the end", "middle of the list", "last k nodes" — anything measured from a place you cannot reach directly.
- An explicit "can you do it in one pass?" follow-up. The two-pass answer (count, then walk length−n) is perfectly correct and worth stating first.
- The cousin trick is fast/slow with a *speed* difference rather than a *position* difference — that finds the middle and detects cycles.

## Where people go wrong

- **No dummy node.** Removing the head (n == length) then needs a whole separate branch. The dummy erases it.
- **Off-by-one in the head start.** `range(n)` vs `range(n+1)` decides whether `left` lands on the victim or on its predecessor. You need the predecessor, so with a dummy start it is exactly `range(n)` plus a `while right.next` loop.
- **`while right` instead of `while right.next`.** Overshoots by one and you delete the wrong node.
- **Not validating n.** LeetCode guarantees it is in range; an interviewer may not.

## The reusable template

```python
# Fixed-gap two pointers - reach an offset from the END in one pass
dummy = ListNode(0, head)
left = right = dummy

for _ in range(n):          # open a gap of exactly n
    right = right.next

while right.next:           # walk together until right is the LAST node
    right = right.next
    left  = left.next

left.next = left.next.next  # left is the victim's predecessor
return dummy.next
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Middle of the list** (LC 876 / 2095) | Speed gap, not position gap: slow one step, fast two. |
| **Cycle detection** (LC 141 / 142) | Same fast/slow, but the question is whether they ever meet. |
| Nth from the end without deleting | Identical setup, just return `left.next`. |
| Doubly linked list | Walk backwards from the tail. The whole trick becomes unnecessary. |

## How to think about it next time

Two pointer separations, two different jobs. **Fixed position gap** (this problem): they move at the same speed, so the distance is constant — use it to reach a fixed offset from the end. **Fixed speed ratio** (fast/slow): the distance grows, which is what finds the midpoint and closes cycles. Ask "do I need a constant offset or a constant ratio?" and the right tool is obvious.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list)
