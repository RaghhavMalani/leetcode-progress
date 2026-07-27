# 143. Reorder List
> **Medium** &nbsp;·&nbsp; Linked list · compose three primitives &nbsp;·&nbsp; family: **Linked lists**

Not one algorithm but three you already know, in sequence: find the middle, reverse the back half, interleave. The single most important line is `slow.next = None`.

**▶ [Step through this solution line by line](../visualizations/0143-reorder-list.html)** — 21 steps, traced on `head = [1,2,3,4]`.

| | |
|---|---|
| time | O(n) — three linear passes |
| space | O(1) |

## The idea

This is a **composition** problem. Interviewers use it to check whether your primitives are solid enough to be used as building blocks without re-deriving them. If reversing a list is still something you have to think about, you will run out of working memory here.

## How to recognise it

- The target order pairs the first element with the last, second with second-last, and so on. Any time indices pair up as i with n−1−i in a structure with no random access, "reverse the second half" is the move.
- Same decomposition solves palindrome-linked-list (LC 234) and is half of sort-list (LC 148).
- The O(1) space demand is what rules out the easy answer of dumping everything into an array.

## Where people go wrong

- **Forgetting `slow.next = None`.** The two halves stay joined, the weave creates a cycle, and your test hangs instead of failing. Worst possible failure mode.
- **Interleaving with the wrong loop condition.** `while second` is right for this split; `while first and second` can leave a stray link. Test on both n = 4 and n = 5.
- **Not saving both successors in phase 3.** You overwrite `first.next` and then need it. Two temporaries, no shortcuts.
- **Using an array of nodes.** O(n) space, and it makes the problem trivial — which is exactly why the constraint exists.

## The reusable template

```python
# Reorder = middle + reverse + weave
slow = fast = head                       # 1. middle
while fast and fast.next:
    slow, fast = slow.next, fast.next.next

second, slow.next = slow.next, None      # CUT. do not skip this.

prev = None                              # 2. reverse the back half
while second:
    second.next, prev, second = prev, second, second.next

first, second = head, prev               # 3. weave
while second:
    n1, n2 = first.next, second.next
    first.next, second.next = second, n1
    first, second = n1, n2
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Palindrome Linked List** (LC 234) | Middle, reverse, then compare instead of weave. |
| **Sort List** (LC 148) | Middle to split, recurse on both, merge. |
| Reorder an array | Trivial with two indices — the difficulty here is entirely the lack of random access. |
| Reverse in k-groups | LC 25 — the reversal primitive applied repeatedly. The hardest in the family. |

## How to think about it next time

When a list problem looks intimidating, try to **write the solution as three sentences before writing any code**. Here: "cut it in half; reverse the back; zip them." If you can say it in sentences and each sentence is a primitive you own, the code is mechanical. If a sentence is not a primitive yet, that is the sub-problem to go and drill. This decomposition habit is what separates people who solve Mediums reliably from people who solve them when they happen to have seen the trick.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/reorder-list)
