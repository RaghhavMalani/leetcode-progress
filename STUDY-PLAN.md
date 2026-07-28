# Study plan — the next 30

*Generated from what is actually thin in this repo. Every entry says **why it earns a slot** and **which trace you
already have that it builds on**, so nothing here is a cold start.*

## The gap, measured

| Family | You have | Verdict |
|---|---|---|
| Backtracking | 9 | healthy |
| Two pointers & sliding window | 13 | healthy |
| Hashing | 13 | healthy |
| Linked lists | 8 | healthy |
| Stacks & monotonic stacks | 3 | **thin — fill this** |
| Binary search | 3 | **thin — fill this** |
| Trees | 3 | **thin — fill this** |
| Graphs, BFS & DFS | 8 | healthy |
| Dynamic programming | 6 | adequate |
| Greedy | 10 | healthy |
| Prefix sums & intervals | 9 | healthy |
| Bit manipulation | 4 | **thin — fill this** |
| Math & number theory | 11 | healthy |
| Design | 3 | **thin — fill this** |
| Sorting & divide and conquer | 3 | **thin — fill this** |
| Brute force done right | 3 | **thin — fill this** |

Overall: **35 Easy / 58 Medium / 16 Hard**. Four families sit at three problems each, and they are exactly the four
that interviews lean on hardest. Your DP is six problems but skews Hard — you have solved digit DP and matrix
exponentiation without ever solving House Robber, which is backwards.

The plan below is five waves of six. Do them **in order within a wave**, and do not start a new wave until you can
reassemble the previous one from memory in the Dojo.

---

## Wave 1 · Trees (you have 3 — this is the biggest hole)

You have inorder traversal, max path sum, and build-from-descriptions. That is an odd, top-heavy selection: you can
do the Hard one but not the fundamentals it is built from.

| # | Problem | Why this one | Builds on |
|---|---|---|---|
| 104 | Maximum Depth of Binary Tree | The simplest possible postorder. Establishes "a node returns something to its parent". | — |
| 226 | Invert Binary Tree | Mutation during traversal, and the famous interview question. | 104 |
| 543 | Diameter of Binary Tree | **The direct sibling of your 124** — same "return one thing, track another", with counts instead of sums. Solve it and then re-read your 124 notes; they will click properly. | [124](visualizations/0124-binary-tree-maximum-path-sum.html) |
| 110 | Balanced Binary Tree | Returning two facts at once (height + is-balanced), or a sentinel. Teaches early termination. | 543 |
| 102 | Binary Tree Level Order Traversal | The `for _ in range(len(queue))` idiom — which **your 3558 already uses** without you having drilled it. | [3558](visualizations/3558-number-of-ways-to-assign-edge-weights-i.html) |
| 98 | Validate BST | Inorder must be increasing, or pass down (low, high). Makes the point of **your 94** concrete. | [94](visualizations/0094-binary-tree-inorder-traversal.html) |

**Then, when the wave is solid:** 230 (kth smallest — early-exit inorder), 236 (LCA — the prerequisite for
[3559](visualizations/3559-number-of-ways-to-assign-edge-weights-ii.html), which you solved *without* it), 105
(build from preorder + inorder).

---

## Wave 2 · Binary search (you have 3, and one is a Hard variant)

You solved 81 — rotated **with duplicates** — without ever solving 33, the clean version. Fix the order.

| # | Problem | Why this one | Builds on |
|---|---|---|---|
| 35 | Search Insert Position | The **boundary form** (`return lo` after the loop). Half of all binary search problems are this shape, not the exact-match one. | [704](visualizations/0704-binary-search.html) |
| 33 | Search in Rotated Sorted Array | The clean version of the problem you already did the hard way. Solve it, then diff against your 81. | [81](visualizations/0081-search-in-rotated-sorted-array-ii.html) |
| 153 | Find Minimum in Rotated Sorted Array | Same structure, no target — trains "compare against the right end". | 33 |
| 875 | Koko Eating Bananas | **Binary search on the answer.** This is the single highest-value idea in the family, and your [3620](visualizations/3620-network-recovery-pathways.html) already depends on it. | [3620](visualizations/3620-network-recovery-pathways.html) |
| 1011 | Capacity to Ship Packages | Same technique, different `can()`. Do them back to back until writing `can()` is automatic. | 875 |
| 410 | Split Array Largest Sum | The Hard one, and it is the same ten lines with a greedy feasibility check. | 1011 |

---

## Wave 3 · Stacks (you have 3)

You have the monotonic stack (739) and a simulation (682) but not the basics or the hard one.

| # | Problem | Why this one | Builds on |
|---|---|---|---|
| 20 | Valid Parentheses | The canonical matching stack. Everyone asks it. | [682](visualizations/0682-baseball-game.html) |
| 150 | Evaluate Reverse Polish Notation | Pop two, apply, push. Same skeleton as your 682. | 20 |
| 155 | Min Stack | A **second stack of running minima** — your first taste of composing two structures, which is what Design is. | 150 |
| 739 | *(done)* | — | — |
| 853 | Car Fleet | A monotonic stack where the insight is sorting by position first. Trains "the sort key is the algorithm". | [739](visualizations/0739-daily-temperatures.html) |
| 84 | Largest Rectangle in Histogram | The Hard boss of the family. Do it **after** 739 and 42 — you already have both. | [739](visualizations/0739-daily-temperatures.html), [42](visualizations/0042-trapping-rain-water.html) |
| 496 | Next Greater Element I | A gentle re-run of 739 to confirm the pattern transferred. | [739](visualizations/0739-daily-temperatures.html) |

---

## Wave 4 · Design (you have 3, two of which are dict wrappers)

Your 705 and 706 wrap Python's `dict` rather than implementing a hash table — see [REFACTOR.md](REFACTOR.md). Your
146 and 460 are genuinely good. What is missing is the middle: composing a map with *one other* structure.

| # | Problem | Why this one | Builds on |
|---|---|---|---|
| 380 | Insert Delete GetRandom O(1) | Map + array, delete by swapping with the last element. The cleanest "two structures, cross-referenced" problem there is. | [146](visualizations/0146-lru-cache.html) |
| 208 | Implement Trie | Your first tree-shaped data structure built from scratch. | — |
| 211 | Design Add and Search Words | Trie + backtracking on `.` — **combines wave 4 with your strongest family**. | 208, [22](visualizations/0022-generate-parentheses.html) |
| 295 | Find Median from Data Stream | Two heaps balanced against each other. The natural sequel to your [703](visualizations/0703-kth-largest-element-in-a-stream.html). | [703](visualizations/0703-kth-largest-element-in-a-stream.html) |
| 981 | Time Based Key-Value Store | Map → sorted list → binary search. Ties wave 2 to wave 4. | 35 |
| 355 | Design Twitter | Map + heap + merge of k feeds. Pulls in your [23](visualizations/0023-merge-k-sorted-lists.html). | [23](visualizations/0023-merge-k-sorted-lists.html) |

---

## Wave 5 · DP fundamentals (you skipped the bottom of the ladder)

You have solved digit DP and matrix exponentiation. You have not solved House Robber. That is a real gap: the Hard
DP you can do is pattern-matched, not derived.

| # | Problem | Why this one | Builds on |
|---|---|---|---|
| 198 | House Robber | Structurally identical to your [70](visualizations/0070-climbing-stairs.html) — `max` instead of `+`, skip the neighbour. Prove that to yourself. | [70](visualizations/0070-climbing-stairs.html) |
| 213 | House Robber II | Circular — run the linear version twice on two slices. Teaches "reduce the new case to the old one". | 198 |
| 53 | Maximum Subarray | Kadane. The most-asked DP in existence, and you do not have it. | 198 |
| 152 | Maximum Product Subarray | Track the running **min as well as the max**, because a negative flips them. Pairs with your [628](visualizations/0628-maximum-product-of-three-numbers.html). | 53 |
| 322 | Coin Change | Unbounded knapsack — the *counting* twin of your [39](visualizations/0039-combination-sum.html). Solve it and compare the two directly. | [39](visualizations/0039-combination-sum.html) |
| 300 | Longest Increasing Subsequence | O(n²) then the O(n log n) patience version, which needs wave 2. Also the engine behind Russian Doll Envelopes, the sequel to your [1288](visualizations/1288-remove-covered-intervals.html). | 35, [1288](visualizations/1288-remove-covered-intervals.html) |

**Then:** 1143 (LCS — your first 2D DP), 416 (subset sum — the *decision* twin of 322), 62 *(done)*, 416 → 494.

---

## How to run a wave

1. **Read nothing first.** Try the problem cold for 20 minutes.
2. If stuck, do not read a solution — open the trace of the problem in the "builds on" column and re-watch it.
3. After you solve it, write the one sentence: *the reusable capability I just implemented is ______*.
4. Add it to the Dojo rotation. A problem you solved once and never revisited is a problem you have not learned.
5. When the wave is done, do a **Boss fight** in the [Dojo](visualizations/dojo.html). If you score below 70%, the
   wave is not finished.

## What "done" looks like

Every family at **6 or more** problems, and the four thin families at 8+. That is roughly 140 problems total —
another 30 on top of your 109. The point is not the number; it is that no family is so thin that an interview
question from it is a coin flip.
