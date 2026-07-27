# 237. Delete Node in a Linked List
> **Medium** &nbsp;·&nbsp; Linked list · impersonation trick &nbsp;·&nbsp; family: **Linked lists**

A lateral-thinking problem. You cannot delete the node you were given, so you make it pretend to be the next one and delete that instead. Note the restriction this creates: it cannot work on the tail.

**▶ [Step through this solution line by line](../visualizations/0237-delete-node-in-a-linked-list.html)** — 4 steps, traced on `head = [4,5,1,9], node = the node with value 1`.

| | |
|---|---|
| time | O(1) |
| space | O(1) |

## The idea

A node has no identity beyond its value and its link. If you cannot remove a node from the chain, **overwrite its contents with its successor’s and remove the successor** — an observer walking the list cannot tell the difference. The lesson generalises: when you cannot change a structure, ask whether you can change what it *contains*.

## How to recognise it

- You are given a pointer into the middle of a structure with no access to the head or to a parent.
- The problem explicitly promises the node is not the tail — that promise is load-bearing, since there would be nothing to impersonate.
- Similar shape: deleting from a BST when you only have the node, deleting the middle of an array by copying the last element over it.

## Where people go wrong

- **Trying to null the node out.** `node = None` rebinds a local name; the list is untouched. This is the same trap as `s = s[::-1]` in LC 344.
- **Assuming it works on the tail.** It cannot — `node.next.val` throws. If the interviewer removes the guarantee, the honest answer is "impossible without the head".
- **Only copying the value and forgetting to relink.** Then the list has a duplicate.
- **Thinking this is a normal deletion.** It is a value shift. If nodes carried identity — object references held elsewhere — this would be observably wrong, and that is a good caveat to raise.

## The reusable template

```python
# Cannot unlink yourself? Impersonate your successor.
node.val  = node.next.val      # become the next node
node.next = node.next.next     # then delete the next node - you ARE its predecessor

# Requires: node is not the tail.
# Same idea on an array when order does not matter:
#   a[i] = a[-1]; a.pop()
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| With access to the head | Walk to the predecessor and rewire normally. O(n), and the usual case. |
| Doubly linked list | `node.prev.next = node.next` — genuinely O(1), no impersonation. |
| Delete from the middle of an **array** in O(1) | Same idea: copy the last element over the hole and shrink. Only legal when order does not matter. |
| Node is the tail | Impossible. Being able to say why is the point. |

## How to think about it next time

Cheap but real lesson: **separate the structure from its contents.** Interviewers use this problem to see whether you accept "I do not have a pointer to the previous node, therefore I cannot delete" or push past it to "what would an observer actually notice?" Reframing "delete this node" as "make the list look as if this value is gone" is the whole solve — and that reframing habit is what makes hard problems tractable.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/delete-node-in-a-linked-list)
