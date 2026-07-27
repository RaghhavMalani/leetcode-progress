# 94. Binary Tree Inorder Traversal
> **Easy** &nbsp;·&nbsp; Tree traversal · explicit stack &nbsp;·&nbsp; family: **Trees**

The iterative inorder. The recursive version is four lines; this one exists so you understand what the call stack was doing — and because problems like BST Iterator demand a traversal you can pause.

**▶ [Step through this solution line by line](../visualizations/0094-binary-tree-inorder-traversal.html)** — 23 steps, traced on `root = [1,null,2,3]`.

| | |
|---|---|
| time | O(n) — every node pushed once, popped once |
| space | O(h) — h = height; O(n) for a degenerate tree |

## The idea

Recursion *is* a stack. Making it explicit costs a few lines and buys two things: no recursion-depth limit, and the ability to **stop halfway** and resume — which is the entire point of an iterator. The pattern is: dive left pushing everything, pop-and-output, then pivot right and repeat.

## How to recognise it

- **Inorder** on a BST gives sorted order. That single fact solves LC 98 (validate BST), LC 230 (kth smallest), LC 173 (iterator), and LC 501.
- Preorder (node, left, right) is for **copying / serialising** — you see a node before its children.
- Postorder (left, right, node) is for **aggregating upward** — children before parent. LC 124 in your repo is postorder.
- Level order needs a queue, not a stack — that is BFS.

## Where people go wrong

- **Getting the loop guard wrong.** It must be `while curr or stack`. Just `while stack` exits immediately at the start; just `while curr` never comes back up.
- **Outputting on push instead of on pop.** That gives preorder, not inorder. The whole distinction between the three orders is *when you emit the node*.
- **Forgetting `curr = curr.right` after popping.** Then you re-dive on the same node forever.
- **Recursion depth.** Python defaults to 1000 frames; a 10⁴-node skewed tree crashes the recursive version. Worth saying aloud.

## The reusable template

```python
# Iterative inorder - dive left, pop-and-emit, pivot right
stack, res, curr = [], [], root
while curr or stack:
    while curr:                 # dive as far left as possible
        stack.append(curr)
        curr = curr.left
    curr = stack.pop()          # leftmost unvisited node
    res.append(curr.val)        # EMIT here -> inorder
    curr = curr.right           # now treat the right subtree as a fresh tree

# preorder : emit when you PUSH        (node, left, right)
# postorder: emit on the way back up   (left, right, node)  - recursion is easier
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **BST Iterator** (LC 173) | This exact loop, split across `next()` and `hasNext()`. The reason to learn the iterative form. |
| **Kth Smallest in a BST** (LC 230) | Inorder and stop after k pops — no need to traverse the whole tree. |
| **Validate BST** (LC 98) | Inorder must be strictly increasing; or pass down (low, high) bounds. |
| **Morris traversal** | O(1) space by temporarily rewiring right pointers into threads. Impressive, rarely required, worth knowing it exists. |
| Level order | LC 102 — a queue and a loop over each level’s size. |

## How to think about it next time

Fix the three orders by **what they are for**, not by their names. Need children answered before the parent (heights, sums, max path)? **Postorder**. Need to visit a node before descending (serialise, copy, path-building)? **Preorder**. Need sorted order from a BST? **Inorder**. When you meet a tree problem, ask "does a node need information from its children?" — if yes, you are writing postorder and the recursion returns a value; if no, you are writing preorder and it carries a value downward.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/binary-tree-inorder-traversal)
