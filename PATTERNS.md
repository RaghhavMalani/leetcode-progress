# Pattern handbook

*A companion to the traced visualizations in [`visualizations/index.html`](visualizations/index.html).
Every claim below is illustrated by at least one problem you have already solved in this repository — the links go
straight to a step-by-step replay of **your own code**.*

---

## How to attack a problem you have not seen

1. **Read the constraints first, and read them as information.** They tell you the target complexity and often the
   whole approach. They also hide structural gifts — "sorted", "a permutation of 1..n", "all values ≤ 200",
   "preserve the relative order". Each of those changes the answer.
2. **Say what the answer *is*.** Count, list, best value, or yes/no? *List all* → backtracking. *Count* → DP or a
   combinatorial argument. *Best value* → greedy, DP, or binary-search-the-answer. Getting this wrong costs you the
   whole problem.
3. **State the brute force out loud and price it.** If it fits, write it well. If it does not, the gap between it and
   the constraints tells you which factor you have to remove.
4. **Name the pattern before you type.** One sentence: "this is a sliding window where the window is invalid when…".
   If you cannot finish that sentence, you are not ready to write code.
5. **Write the invariant in a comment.** "If the answer exists it is in [lo, hi]". "Everything left of `low` is a
   settled 0." Then check that every branch preserves it. Most in-place pointer bugs die on paper here.
6. **Trace it on the smallest interesting input.** Not [1,2,3] — the one with a duplicate, or an empty half, or a
   single element.

### Target complexity from the constraint

| n up to | expected | typical technique |
|---|---|---|
| 10–20 | O(2ⁿ), O(n!) | backtracking, bitmask DP |
| 100 | O(n³) | triple loop, Floyd–Warshall, interval DP |
| 1 000 | O(n²) | DP tables, pairwise scans |
| 10⁵–10⁶ | O(n log n) | sorting, heap, binary search, Fenwick |
| 10⁵–10⁶ | O(n) | two pointers, prefix sums, monotonic stack, counting |
| 10⁹ | O(log n) or O(1) | binary search on the answer, math, closed form |
| 10¹⁸ | O(log n) | matrix exponentiation, fast exponentiation, periodicity |

---

## The reductions worth memorising

These are the moves that turn a hard problem into an easy one. Most Hard problems are two or three of them chained.

| When you see | Reduce it to |
|---|---|
| "more X than Y in a range" | map X→+1, Y→−1; **positive sum** |
| "sum/count over a range", static data | **prefix sums**; range updates → difference array |
| "for each i, something about all the others" | **prefix × suffix** |
| "count pairs i<j with p[i] < p[j]" | **inversion count** — Fenwick or merge sort |
| "maximise the minimum" / "minimise the maximum" | **binary search the answer** + a feasibility check |
| "minimum number of operations to reach a goal" | **BFS on a state graph** |
| "distance to the nearest of many sources" | **multi-source BFS** |
| "next greater / smaller element" | **monotonic stack** |
| "kth largest, streaming" | **size-k min-heap** |
| "sum over all subsets/subarrays" | **contribution technique** — flip the order of summation |
| "count numbers in [L,R] with a digit property" | **digit DP**, and `f(R) − f(L−1)` |
| "follow this pointer many times, many times over" | **binary lifting** |
| "same transition, n up to 10¹⁸" | **matrix exponentiation** |
| an array of indices | a **functional graph** — cycle detection applies |

---

## A debugging checklist

When a solution is wrong and you cannot see why, walk this list before re-reading the code:

- **Empty input, single element, all-equal elements, all-negative elements.**
- **Off-by-one in an inclusive range.** Length is `r - l + 1`. Write it out.
- **Did I store a reference where I meant a copy?** (`res.append(path)` vs `path.copy()`)
- **Did I update state before or after using it?** Prefix/suffix accumulation and the `max2 = max1` demotion both
  depend on the order.
- **Did I mark visited on enqueue or on dequeue?** BFS wants enqueue; lazy-deletion Dijkstra wants pop.
- **Do all my parallel structures agree?** Every design bug lives here.
- **Does my loop condition cover the tail?** Run-scanning code almost always forgets the run that ends at the end.
- **Am I comparing indices when I mean values, or values when I mean indices?**

---

## Backtracking
*Choose → explore → un-choose. One shared mutable path, mutated on the way down and rewound on the way up. Everything else in this family is a different guard on the same skeleton.*
**The mechanic.** One shared mutable list. Push a choice, recurse, pop it. That is the entire pattern; every problem in
the family is that skeleton with different guards.

```python
def backtrack(state):
    if is_complete(state):
        res.append(path.copy())      # COPY. path keeps mutating.
        return
    if is_impossible(state):         # prune BEFORE you descend
        return
    for choice in choices(state):
        path.append(choice)          # 1. choose
        backtrack(advance(state))    # 2. explore
        path.pop()                   # 3. un-choose
```

**Recognise it.** "Find **all**…" (not "count", not "the best") · exponential output with tiny constraints
(n ≤ 20) · each answer is a sequence of decisions · a partial answer can be judged as still-valid or already-doomed.

**The two dialects.** *Take/skip* makes one binary decision per element (78, 39, 90). *Loop form* iterates over the
choices available at this level (77, 46, 47). They are interchangeable — practise converting between them, because
after that "subset problems" and "combination problems" stop looking different.

**Killing duplicate answers.** Two idioms, pick one and know why:
- **sort + skip equal neighbours** on the *skip* branch (40, 90)
- **loop over distinct values with a count budget** (47)

**The four bugs.**
1. `res.append(path)` instead of `path.copy()` — you store a reference and the next `pop()` corrupts it.
2. Forgetting the `pop()` — the next branch inherits polluted state.
3. Validating at the leaf instead of at the branch — correct but exponentially slower. Compare 22 (zero dead ends)
   with 39 (mostly dead ends) side by side; that gap is the whole lesson.
4. Skipping duplicates on the *take* branch instead of the *skip* branch.

**How to think about it.** Answer three questions out loud before writing anything: *what is one choice?*, *when am
I done?*, *what makes a choice illegal, and can I test that before I make it?* If the answer to the third is "only at
the end", your solution will be correct and slow — and closing that gap is usually what the problem is testing.

**Traced in this repo** — start with **22 vs 39**:

| # | Problem | Difficulty | The specific idea |
|---|---|---|---|
| 22 | [Generate Parentheses](visualizations/0022-generate-parentheses.html) | Medium | Backtracking · build-and-undo |
| 39 | [Combination Sum](visualizations/0039-combination-sum.html) | Medium | Backtracking · take / skip |
| 40 | [Combination Sum II](visualizations/0040-combination-sum-ii.html) | Medium | Backtracking · duplicate suppression |
| 46 | [Permutations](visualizations/0046-permutations.html) | Medium | Recursion · bottom-up construction (NOT backtracking) |
| 47 | [Permutations II](visualizations/0047-permutations-ii.html) | Medium | Backtracking · counter as state |
| 77 | [Combinations](visualizations/0077-combinations.html) | Medium | Backtracking · loop form |
| 78 | [Subsets](visualizations/0078-subsets.html) | Medium | Backtracking · take / skip |
| 90 | [Subsets II](visualizations/0090-subsets-ii.html) | Medium | Backtracking · duplicate suppression |
| 291 | [Word Pattern II](visualizations/0291-word-pattern-ii.html) | Medium | Backtracking · bijection search |

---

## Two pointers & sliding window
*Two indices that only ever move forward. The window grows on the right and shrinks on the left, so the total work is 2n even when the code looks nested.*
**The mechanic.** Two indices that only ever move forward. Because neither rewinds, an inner `while` is *not* a nested
loop — the total work is 2n. If you ever reset `l` back to `r`, you have left the pattern and gone quadratic.

```python
left = 0
for right in range(len(s)):
    add(s[right])                       # grow
    while window_is_invalid():          # shrink until legal again
        remove(s[left]); left += 1
    ans = best(ans, right - left + 1)   # record
```

**Three flavours.** *Variable size* (3, 1358) — grow right, shrink left with a `while`. *Fixed size* (219) — no
`while`, just add one and drop one. *Converging* (42, 344, 75) — start at both ends and walk inward.

**Recognise it.** The word **substring** or **subarray** (contiguous!) — never "subsequence" · longest / shortest /
count of stretches with a property · the property is monotone: growing the window cannot fix an invalid one.

**Counting variant.** When a window is valid and every extension of it is also valid, count a whole batch at once:
`ans += n - right`. When the property is *not* monotone ("exactly k distinct"), decompose it:
`exactly(k) = atMost(k) - atMost(k-1)`. Those two tricks cover almost every "count the subarrays" problem.

**Fast & slow** is the other half of this family: two pointers at different *speeds* rather than different positions.
It does three jobs — detect a cycle (141), find the middle (2095, 143), and locate a cycle entrance (287, phase two).

**The three questions.** *What makes a window invalid? What do I do to fix it? When do I record?* Record after the
shrink for the longest, during the shrink for the shortest. If shrinking from the left does not obviously restore
legality, it is probably not a sliding window at all.

**Traced in this repo** — start with **3, 42, 287**:

| # | Problem | Difficulty | The specific idea |
|---|---|---|---|
| 3 | [Longest Substring Without Repeating Characters](visualizations/0003-longest-substring-without-repeating-characters.html) | Medium | Sliding window · variable size |
| 14 | [Longest Common Prefix](visualizations/0014-longest-common-prefix.html) | Easy | Vertical scanning |
| 19 | [Remove Nth Node From End of List](visualizations/0019-remove-nth-node-from-end-of-list.html) | Medium | Linked list · two pointers with a gap |
| 42 | [Trapping Rain Water](visualizations/0042-trapping-rain-water.html) | Hard | Two pointers · converging |
| 75 | [Sort Colors](visualizations/0075-sort-colors.html) | Medium | Three pointers · Dutch national flag |
| 141 | [Linked List Cycle](visualizations/0141-linked-list-cycle.html) | Easy | Fast & slow pointers · Floyd |
| 219 | [Contains Duplicate II](visualizations/0219-contains-duplicate-ii.html) | Easy | Sliding window · fixed size |
| 287 | [Find the Duplicate Number](visualizations/0287-find-the-duplicate-number.html) | Medium | Floyd cycle detection · fast & slow |
| 344 | [Reverse String](visualizations/0344-reverse-string.html) | Easy | Two pointers · converging |
| 867 | [New 21 Game](visualizations/0867-new-21-game.html) | Medium | Probability DP · sliding window sum |
| 1358 | [Number of Substrings Containing All Three Characters](visualizations/1358-number-of-substrings-containing-all-three-characters.html) | Medium | Sliding window · counting |
| 2095 | [Delete the Middle Node of a Linked List](visualizations/2095-delete-the-middle-node-of-a-linked-list.html) | Medium | Fast & slow pointers · find the middle |
| 2161 | [Partition Array According to Given Pivot](visualizations/2161-partition-array-according-to-given-pivot.html) | Medium | Stable three-way partition |

---

## Hashing
*Trade memory for O(1) lookup. Complement lookup, canonical keys, frequency counts — the same reflex applied to raw values, derived values, and signatures.*
**The mechanic.** Spend O(n) memory to turn an O(n) search into an O(1) lookup. Three uses, in increasing order of
sophistication:

1. **Membership** — "have I seen this?" (217, 128)
2. **Complement lookup** — "what would I need to have already seen?" (1, and the whole prefix-sum family)
3. **Canonical key** — "what is the smallest piece of data that decides sameness?" (49, 288, 36)

```python
seen = {}                             # complement lookup: look up BEFORE inserting
for i, x in enumerate(nums):
    if target - x in seen: return [seen[target - x], i]
    seen[x] = i

groups = defaultdict(list)            # canonical key: group without pairwise comparison
for item in items:
    groups[canonical(item)].append(item)
```

**The big idea most people miss.** Apply the complement trick to *derived* quantities, not just raw values. Not
"have I seen this number" but "have I seen this **running sum**, this **remainder**, this **sorted signature**".
That single generalisation unlocks subarray-sum-equals-k, subarrays divisible by k, and contiguous-array.

**Bugs.** Inserting before looking up (an element pairs with itself) · using a list as a dict key (`TypeError:
unhashable` — wrap it in `tuple()`) · keying by index instead of by value · deduplicating at the *end* after doing
all the exponential work anyway.

**Bucketing.** When the key is a bounded small integer, skip the hash map and index an array directly — that is
counting sort, and it is how 347 beats both sorting and a heap. Always ask: *is my sort key a bounded integer?*

**Traced in this repo** — start with **1, 49, 128**:

| # | Problem | Difficulty | The specific idea |
|---|---|---|---|
| 1 | [Two Sum](visualizations/0001-two-sum.html) | Easy | Hash map · complement lookup |
| 36 | [Valid Sudoku](visualizations/0036-valid-sudoku.html) | Medium | Hash sets · index-to-bucket mapping |
| 49 | [Group Anagrams](visualizations/0049-group-anagrams.html) | Medium | Hash map · canonical key |
| 128 | [Longest Consecutive Sequence](visualizations/0128-longest-consecutive-sequence.html) | Medium | Hash set · amortised scan |
| 138 | [Copy List With Random Pointer](visualizations/0138-copy-list-with-random-pointer.html) | Medium | Hash map old→new · two-pass clone |
| 146 | [LRU Cache](visualizations/0146-lru-cache.html) | Medium | Design · hash map + doubly linked list |
| 217 | [Contains Duplicate](visualizations/0217-contains-duplicate.html) | Easy | Hash set · membership |
| 242 | [Valid Anagram](visualizations/0242-valid-anagram.html) | Easy | Hash map · frequency count |
| 288 | [Unique Word Abbreviation](visualizations/0288-unique-word-abbreviation.html) | Medium | Design · precompute a canonical key |
| 347 | [Top K Frequent Elements](visualizations/0347-top-k-frequent-elements.html) | Medium | Bucket sort · frequency |
| 387 | [First Unique Character in a String](visualizations/0387-first-unique-character-in-a-string.html) | Easy | Hash map · two-pass frequency |
| 2196 | [Create Binary Tree From Descriptions](visualizations/2196-create-binary-tree-from-descriptions.html) | Medium | Hash map · build a structure from edges |
| 3020 | [Find the Maximum Number of Elements in a Subset](visualizations/3020-find-the-maximum-number-of-elements-in-subset.html) | Medium | Frequency map · chain following |

---

## Linked lists
*No random access, so every problem is about not losing your grip on a node. Dummy heads, fast/slow pointers, and save-before-you-overwrite.*
**The mechanic.** No random access, so every problem is really about **not losing your grip on a node**. Overwrite a
`next` pointer without saving it and everything downstream is unreachable.

```python
prev, curr = None, head             # reverse: save, flip, advance, advance
while curr:
    nxt = curr.next                 # 1. SAVE first
    curr.next = prev                # 2. flip
    prev, curr = curr, nxt          # 3-4. advance
return prev                          # prev is the new head
```

**Three helpers that solve most of the family.**
- **Dummy head** — if an operation could touch the head, start with a sentinel. It deletes every "is this the first
  node?" branch at the cost of one line (21, 19, 92).
- **Fast & slow** — finds the middle (2095), detects cycles (141), splits a list (143).
- **Fixed-gap two pointers** — reach an offset *from the end* in one pass (19).

**Reversal is a primitive, not a problem.** It appears as a *step* inside 92 (reverse a slice), 143 (reorder), 234
(palindrome) and 25 (k-groups). Drill it until it is automatic, then compose.

**Bugs.** Flipping before saving (infinite loop) · returning `curr` instead of `prev` · forgetting to cut with
`slow.next = None` before re-joining (creates a cycle — your test *hangs* rather than failing) · advancing by one
after inserting a node when you should advance by two.

**How to think about it.** Draw four nodes and physically point at them as you execute each line. Before mutating,
**name every pointer that will break and where each broken end must end up**. Nearly every bug in this category is
visible in ten seconds on paper and invisible for twenty minutes in your head.

**Traced in this repo** — start with **206, 21, 143**:

| # | Problem | Difficulty | The specific idea |
|---|---|---|---|
| 2 | [Add Two Numbers](visualizations/0002-add-two-numbers.html) | Medium | Linked list · digit-by-digit carry |
| 21 | [Merge Two Sorted Lists](visualizations/0021-merge-two-sorted-lists.html) | Easy | Linked list · dummy head + merge |
| 92 | [Reverse Linked List II](visualizations/0092-reverse-linked-list-ii.html) | Medium | Linked list · partial reversal + seams |
| 143 | [Reorder List](visualizations/0143-reorder-list.html) | Medium | Linked list · compose three primitives |
| 206 | [Reverse Linked List](visualizations/0206-reverse-linked-list.html) | Easy | Linked list · pointer rewiring |
| 237 | [Delete Node in a Linked List](visualizations/0237-delete-node-in-a-linked-list.html) | Medium | Linked list · impersonation trick |
| 622 | [Design Circular Queue](visualizations/0622-design-circular-queue.html) | Medium | Design · doubly linked list with sentinels |
| 2807 | [Insert Greatest Common Divisors in Linked List](visualizations/2807-insert-greatest-common-divisors-in-linked-list.html) | Medium | Linked list · insert between pairs |

---

## Stacks & monotonic stacks
*A stack is a queue of unanswered questions. Keep it sorted and one new fact resolves a whole prefix of them at once.*
**The mechanic.** A stack holds **unanswered questions**, kept in sorted order so that one new fact resolves a whole
prefix of them at once.

```python
stack = []                                  # indices, kept decreasing by value
for i, x in enumerate(a):
    while stack and x > a[stack[-1]]:       # x resolves everything it dominates
        j = stack.pop(); ans[j] = i - j
    stack.append(i)
```

**Recognise it.** "**Next** greater / smaller element", "how long until…", "previous greater" · the brute force is an
O(n²) double loop · histogram areas, stock spans, rain water, remove-k-digits.

**Why it is O(n).** Each index is pushed once and popped once. The nested `while` never makes it quadratic — the same
amortised argument that makes 128 linear. Be ready to say this; it is the follow-up question.

**Greedy + feasibility.** 1081 adds a second condition to the pop: only drop a character if it *reappears later*.
That shape — take the locally best action, but only when it does not make the goal unreachable — recurs constantly
(402 uses a removal budget as its feasibility condition instead).

**Choosing a stack at all.** The data structure is decided by the **hardest single operation**, not the most common
one. In 682, three of the four operations work fine with a running total; the *undo* is what forces a stack.

**Traced in this repo** — start with **739, 1081, 682**:

| # | Problem | Difficulty | The specific idea |
|---|---|---|---|
| 682 | [Baseball Game](visualizations/0682-baseball-game.html) | Easy | Stack · simulation with undo |
| 739 | [Daily Temperatures](visualizations/0739-daily-temperatures.html) | Medium | Monotonic stack · next greater element |
| 1081 | [Smallest Subsequence of Distinct Characters](visualizations/1081-smallest-subsequence-of-distinct-characters.html) | Medium | Monotonic stack · greedy with a safety check |

---

## Binary search
*Not "look in the middle" — maintain an invariant while halving a range. The real power is searching the ANSWER, not the array.*
**The mechanic.** Not "look in the middle" — **maintain an invariant while halving a range**. State the invariant
("if the answer exists it is in [lo, hi]") and every decision follows from keeping it true.

```python
lo, hi = 0, len(a) - 1                # inclusive bounds -> <= in the loop
while lo <= hi:
    mid = lo + (hi - lo) // 2         # never (lo+hi)//2 in a fixed-width language
    if a[mid] == target: return mid
    elif a[mid] < target: lo = mid + 1
    else:                 hi = mid - 1
return -1
```

**The upgrade that matters most.** Stop thinking "binary search needs a sorted array" and start thinking
**"binary search needs a monotone yes/no question"**. Then:

```python
lo, hi, ans = 0, MAX_POSSIBLE, -1     # binary search on the ANSWER
while lo <= hi:
    mid = (lo + hi) // 2
    if can(mid): ans, lo = mid, mid + 1     # feasible -> record, try higher
    else:        hi = mid - 1
return ans
```

"Maximise the minimum" / "minimise the maximum" / "smallest capacity such that…" are all this. The search is always
the same ten lines; the whole problem is writing `can()` and arguing it is monotone (3620, 1631, 2812).

**Bugs.** `<` with inclusive bounds (misses a one-element range) · `hi = mid` with `<=` (infinite loop) ·
`(lo+hi)//2` overflow · recording on the wrong branch when searching the answer · not checking monotonicity at all.

**Locally sorted structures.** When the data is not globally ordered, find the piece that is: a rotated array always
has one sorted half (81); a mountain array has one monotone side. Ask *where do I stand so that a single comparison
eliminates a large chunk?*

**Traced in this repo** — start with **704, 81, 3620**:

| # | Problem | Difficulty | The specific idea |
|---|---|---|---|
| 81 | [Search in Rotated Sorted Array II](visualizations/0081-search-in-rotated-sorted-array-ii.html) | Medium | Binary search · rotated + duplicates |
| 704 | [Binary Search](visualizations/0704-binary-search.html) | Easy | Binary search · exact match |
| 3620 | [Network Recovery Pathways](visualizations/3620-network-recovery-pathways.html) | Hard | Binary search on the answer + DAG shortest path |

---

## Trees
*Decide what a node returns to its parent versus what it contributes to the answer. Get those two sentences right and the recursion writes itself.*
**The mechanic.** For every tree DFS, write two sentences before coding:

> `dfs(node)` **returns** ______ .
> The answer is **updated using** ______ .

If those two sentences are the same, the problem is easy. If they differ — as in 124, where a node returns its best
*downward* path but contributes its best *through* path — you need a global, and knowing that in advance is most of
the solve.

```python
res = [root.val]                       # or: nonlocal res
def dfs(node):
    if not node: return 0
    l = max(dfs(node.left),  0)        # clamp: never take a harmful branch
    r = max(dfs(node.right), 0)
    res[0] = max(res[0], node.val + l + r)   # TRACK: path THROUGH this node
    return node.val + max(l, r)              # RETURN: one branch only
```

**The three orders, by what they are for.** *Postorder* — a node needs answers from its children (heights, sums, max
path). *Preorder* — carry information downward (serialise, copy, build paths). *Inorder* — on a BST this yields
**sorted order**, which alone solves validate-BST, kth-smallest and BST-iterator.

**Iterative traversal** (94) exists so you can pause mid-traversal, and because Python's recursion limit is 1000
while a skewed tree can be 10⁵ deep. Say that out loud.

**Building trees from edges** (2196): a `value → node` map created on demand, and the root is the node that is never
a child. "The root is what nothing points to" also identifies DAG sources and topological-sort starts.

**Many path queries on a static tree** → binary lifting. `up[j][v] = up[j-1][up[j-1][v]]`, LCA in O(log n), and
`dist(u,v) = depth[u] + depth[v] - 2·depth[lca]` (3559).

**Traced in this repo** — start with **124, 94**:

| # | Problem | Difficulty | The specific idea |
|---|---|---|---|
| 94 | [Binary Tree Inorder Traversal](visualizations/0094-binary-tree-inorder-traversal.html) | Easy | Tree traversal · explicit stack |
| 124 | [recursion tree](visualizations/0124-binary-tree-maximum-path-sum.html) | Hard | Tree DFS · return one thing, track another |
| 3559 | [Number of Ways to Assign Edge Weights II](visualizations/3559-number-of-ways-to-assign-edge-weights-ii.html) | Hard | Binary lifting LCA + parity counting |

---

## Graphs, BFS & DFS
*Minimum steps means BFS. Connectivity means DFS or union-find. Weighted means Dijkstra. The hard part is usually recognising that there is a graph at all.*
**Pick the tool from the question.**

| Question | Tool |
|---|---|
| Minimum number of steps, unweighted | **BFS** |
| Is it connected / whole-region property | DFS or union-find |
| Shortest path, non-negative weights | Dijkstra (heap) |
| Shortest path on a **DAG** | Relax in topological order — one linear sweep, no heap |
| Maximise the minimum / minimise the maximum | Dijkstra with `max`/`min` relaxation, **or** binary search the answer, **or** union-find by increasing weight |
| Distance to the nearest of many sources | **Multi-source BFS** — seed them all at distance 0, one sweep |

```python
q, seen = deque([(start, 0)]), {start}        # BFS on a STATE GRAPH
while q:
    state, dist = q.popleft()                 # popLEFT = breadth-first
    if state == target: return dist
    for nxt in neighbours(state):
        if nxt not in seen:
            seen.add(nxt)                     # mark on ENQUEUE, not on dequeue
            q.append((nxt, dist + 1))
return -1
```

**The reframing that unlocks the hard ones.** A node does not have to be a node. In 773 a *board configuration* is a
node and a *move* is an edge. In 287 an *array index* is a node and `i → nums[i]` is an edge. When a problem asks for
"minimum operations to transform X into Y", answer three questions: what is a node, what is an edge, and how do I
encode a node so it is **hashable**.

**Grid DFS.** Mark visited **before** recursing, bounds-check **before** indexing (Python's negative indexing wraps
silently, giving a wrong answer rather than a crash), and decide whether you un-mark: reachability never un-marks,
counting distinct *paths* must.

**Avoid building the graph when the edge structure lets you.** Sorted values with proximity edges collapse to
contiguous runs (3532) — building the adjacency list there would be O(n²) memory for nothing.

**Traced in this repo** — start with **773, 1631, 2812**:

| # | Problem | Difficulty | The specific idea |
|---|---|---|---|
| 463 | [Island Perimeter](visualizations/0463-island-perimeter.html) | Easy | Grid DFS · flood fill |
| 773 | [Sliding Puzzle](visualizations/0773-sliding-puzzle.html) | Hard | BFS on a state graph |
| 1631 | [Path With Minimum Effort](visualizations/1631-path-with-minimum-effort.html) | Medium | Dijkstra · minimax path |
| 2685 | [Count the Number of Complete Components](visualizations/2685-count-the-number-of-complete-components.html) | Medium | Connected components + a counting criterion |
| 2812 | [Find the Safest Path in a Grid](visualizations/2812-find-the-safest-path-in-a-grid.html) | Medium | Multi-source BFS + maximin Dijkstra |
| 3532 | [Path Existence Queries in a Graph I](visualizations/3532-path-existence-queries-in-a-graph-i.html) | Medium | Sorted structure collapses a graph |
| 3534 | [Path Existence Queries in a Graph II](visualizations/3534-path-existence-queries-in-a-graph-ii.html) | Hard | Sort + greedy farthest + binary lifting |
| 3558 | [Number of Ways to Assign Edge Weights I](visualizations/3558-number-of-ways-to-assign-edge-weights-i.html) | Medium | BFS height + parity counting |

---

## Dynamic programming
*Four questions: what is the state, what is the recurrence, what are the base cases, in what order do I fill it. Then a fifth: how far back does the recurrence reach?*
**Five questions, in order.**

1. **What is the state?** The smallest piece of information about the past that determines the future.
2. **What is the recurrence?** Ask *what was the last decision?* — that generates it almost every time.
3. **What are the base cases?** (ways(0) = 1, not 0. The empty object counts.)
4. **In what order do I fill it?**
5. **How far back does the recurrence reach?** If it is a small constant, throw away the array and keep that many
   variables (70 → two ints, 62 → one row).

**The optimisation that decides accepted vs TLE.** Look at the transition. Is it a **sum or an extremum over a
contiguous window** of previous states? Then drop a whole factor:

| Transition shape | Replace the inner loop with |
|---|---|
| `dp[i] = Σ dp[i-1 … i-w]` | rolling window sum (867) |
| `dp[x] = Σ dp'[y] for y < x` | running prefix sum (3699) |
| `dp[i] = max(dp[i-1 … i-w])` | monotonic deque |
| same linear transition, n up to 10¹⁸ | **matrix exponentiation**, O(dim³ log n) (3700) |

**Choosing a small state.** 3336 cannot track which elements went into which group (3ⁿ) — but it only *needs* the two
gcds, and gcds of values ≤ 200 are ≤ 200. A suspiciously small value bound in a counting problem is nearly always
the intended state dimension.

**Digit DP** is a template with three slots — `tight`, `started`, and whatever context the property needs (3753).
Learn it once and every "count numbers in [L,R] such that…" problem is just deciding the context slot. Always reduce
a range to `solve(R) - solve(L-1)`.

**Counting vs listing.** "How many ways" → DP. "List all the ways" → backtracking. Getting this backwards is the most
expensive mistake in the whole taxonomy.

**Traced in this repo** — start with **70, 62, 3699**:

| # | Problem | Difficulty | The specific idea |
|---|---|---|---|
| 62 | [Unique Paths](visualizations/0062-unique-paths.html) | Medium | Grid DP · rolling row |
| 70 | [Climbing Stairs](visualizations/0070-climbing-stairs.html) | Easy | DP · Fibonacci with rolling variables |
| 3336 | [Find the Number of Subsequences With Equal GCD](visualizations/3336-find-the-number-of-subsequences-with-equal-gcd.html) | Hard | DP over a bounded state (gcd × gcd) |
| 3699 | [Number of Zigzag Arrays I](visualizations/3699-number-of-zigzag-arrays-i.html) | Hard | DP with direction state + prefix-sum transitions |
| 3700 | [Number of Zigzag Arrays II](visualizations/3700-number-of-zigzag-arrays-ii.html) | Hard | Matrix exponentiation of a linear recurrence |
| 3753 | [Total Waviness of Numbers in Range II](visualizations/3753-total-waviness-of-numbers-in-range-ii.html) | Hard | Digit DP · tight / started / carried context |

---

## Greedy
*A greedy you cannot justify is a greedy you will misapply. Always pair it with an exchange argument or a decomposition proof.*
**The rule.** A greedy you cannot justify is a greedy you will misapply. Spend thirty seconds proving it *before*
you write it. There are only two proof shapes you need:

- **Exchange argument** — "swapping any solution towards the greedy choice never makes it worse" (860: a $10 note is
  useless except as change for a $20, so spend it first; 1833: swap any bought item for a cheaper unbought one).
- **Decomposition** — "the total is a sum of independent local terms, so take every positive one" (122: a multi-day
  hold earns exactly the sum of its daily deltas).

**The sort direction is the algorithm.** It is decided by which side of the trade you want to be large:

| Goal | Sort |
|---|---|
| Maximise the **count** under a budget | ascending (1833) |
| Maximise the value of what you get **free** | descending (2144) |
| Keep as many non-overlapping items as possible | by **end** time |
| Merge / insert intervals | by **start** |
| Containment / dominance | by (start asc, end **desc**) — the tie-break *is* the correctness argument (1288) |

**One-directional operations.** When an operation only goes one way (decrease-only, remove-only), that asymmetry
usually decides the processing order. Decrease-only + rearrange → sort ascending and climb (1846). Decrease-only with
a fixed order → start from the **unconstrained end** and work backwards (2450).

**Know when greedy dies.** Add a constraint that links decisions — a transaction fee, a cooldown, "at most k" — and
the decomposition collapses. That is the line between 122 (greedy) and 188/309/714 (DP).

**Traced in this repo** — start with **122, 1288, 2450**:

| # | Problem | Difficulty | The specific idea |
|---|---|---|---|
| 122 | [Best Time to Buy and Sell Stock II](visualizations/0122-best-time-to-buy-and-sell-stock-ii.html) | Medium | Greedy · decompose into local gains |
| 860 | [Lemonade Change](visualizations/0860-lemonade-change.html) | Easy | Greedy · spend the least flexible resource first |
| 1291 | [Sequential Digits](visualizations/1291-sequential-digits.html) | Medium | Generate the small candidate set, then filter |
| 1448 | [Maximum 69 Number](visualizations/1448-maximum-69-number.html) | Easy | Greedy · positional value |
| 1833 | [Maximum Ice Cream Bars](visualizations/1833-maximum-ice-cream-bars.html) | Medium | Greedy · counting sort |
| 1846 | [Maximum Element After Decreasing and Rearranging](visualizations/1846-maximum-element-after-decreasing-and-rearranging.html) | Medium | Greedy · sort then climb |
| 2144 | [Minimum Cost of Buying Candies With Discount](visualizations/2144-minimum-cost-of-buying-candies-with-discount.html) | Easy | Greedy · sort descending, take every third |
| 2450 | [Minimum Replacements to Sort the Array](visualizations/2450-minimum-replacements-to-sort-the-array.html) | Hard | Greedy from the right · equal splitting |
| 2503 | [Longest Subarray With Maximum Bitwise AND](visualizations/2503-longest-subarray-with-maximum-bitwise-and.html) | Medium | Observation-driven · monotone operation |
| 3689 | [Maximum Total Subarray Value I](visualizations/3689-maximum-total-subarray-value-i.html) | Medium | Observation · the constraint that is not there |

---

## Prefix sums & intervals
*Precompute so that queries are cheap. Prefix sums, difference arrays, inclusion–exclusion, and sort-key-driven interval sweeps.*
**The mechanic.** Precompute a value at every position so that any range answer is a cheap combination of two (or
four) of them. It works whenever the operation has an **inverse**.

```python
prefix[j+1] - prefix[i]                       # 1D range sum
prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]   # 2D, inclusion–exclusion
```

**Choose the right member of the family.**

| You need | Use |
|---|---|
| Point updates, many range queries | prefix sums (304) |
| **Range** updates, point queries | **difference array**: `d[l] += x; d[r+1] -= x`, then one prefix pass |
| Both, online | Fenwick tree / segment tree (3739) |
| Suffix as well as prefix, invertible op | `total - prefix - self` — one pass (2574) |
| Suffix as well as prefix, **not** invertible (max, min, gcd) | two passes (238, 42) |

**"Two passes, one forward and one backward"** is worth naming for yourself. It solves 238, 42, 1840 and Candy —
every problem where each position depends on both what came before and what comes after.

**The ±1 transform.** "More X than Y in this range" becomes "positive sum in this range" becomes "prefix[j] >
prefix[i]" becomes an inversion count. That chain is the entire content of 3739, and it also solves
contiguous-array and count-of-range-sums.

**Intervals** live here too, because the sort key does all the work — see the Greedy table above. Three cases cover
every insertion: entirely after (stop), entirely before (copy), overlapping (**absorb, do not append yet**) (57).

**Traced in this repo** — start with **238, 304, 3739**:

| # | Problem | Difficulty | The specific idea |
|---|---|---|---|
| 57 | [Insert Interval](visualizations/0057-insert-interval.html) | Medium | Intervals · three-case scan |
| 238 | [Product of Array Except Self](visualizations/0238-product-of-array-except-self.html) | Medium | Prefix / suffix accumulation |
| 304 | [Range Sum Query 2D — Immutable](visualizations/0304-range-sum-query-2d-immutable.html) | Medium | 2D prefix sum · inclusion–exclusion |
| 1288 | [Remove Covered Intervals](visualizations/1288-remove-covered-intervals.html) | Medium | Intervals · sort key does the work |
| 1732 | [Find the Highest Altitude](visualizations/1732-find-the-highest-altitude.html) | Easy | Prefix sum · running maximum |
| 1840 | [Maximum Building Height](visualizations/1840-maximum-building-height.html) | Hard | Constraint propagation · two sweeps + geometry |
| 2574 | [Left and Right Sum Differences](visualizations/2574-left-and-right-sum-differences.html) | Easy | Prefix sum · total minus prefix |
| 3499 | [Maximize Active Section With Trade I](visualizations/3499-maximize-active-section-with-trade-i.html) | Medium | Run-length scan · pair of adjacent runs |
| 3739 | [Count Subarrays With Majority Element II](visualizations/3739-count-subarrays-with-majority-element-ii.html) | Hard | +1/−1 transform · prefix sums · Fenwick tree |

---

## Bit manipulation
*XOR cancels pairs, AND only clears bits, OR only sets them. That monotonicity usually IS the algorithm.*
**The identities.** Six lines, and almost every bit problem is one of them applied once.

```python
x ^ x == 0        x ^ 0 == x        # XOR: self-inverse -> pairs cancel   (136)
x & (x - 1)                          # clears the lowest set bit
x & -x                               # isolates the lowest set bit
x >> k & 1                           # read bit k
x | (1 << k)                         # set bit k
n.bit_length()                       # how many bits n needs              (3513)
```

**Monotonicity is usually the algorithm.** AND only ever *clears* bits, so the largest AND of any subarray is
`max(nums)` and the problem collapses to a run-length scan (2503). OR only ever *sets* bits, so the set of ORs of
subarrays ending at index i has at most ~32 members and you can carry the whole frontier (934). Ask: *as I extend,
how many distinct values can this aggregate take?* Bounded by the bit width → near-linear algorithm for free.

**The contribution technique.** For "sum over all subsets / subarrays / pairs", **flip the order of summation**:
instead of Σ over objects of (value), compute Σ over components of (component × how many objects contain it).
1863 becomes `OR(nums) × 2^(n-1)` because each set bit survives the XOR in exactly half the subsets. The same move
solves sum-of-subarray-minimums and sum-of-subarray-ranges.

**The meta-signal.** When a problem demands O(1) space on integer data, bits are usually the intended route.

**Traced in this repo** — start with **136, 2503, 1863**:

| # | Problem | Difficulty | The specific idea |
|---|---|---|---|
| 136 | [Single Number](visualizations/0136-single-number.html) | Easy | Bit manipulation · XOR cancellation |
| 934 | [Bitwise ORs of Subarrays](visualizations/0934-bitwise-ors-of-subarrays.html) | Medium | Monotone bit operation · bounded frontier |
| 1863 | [Sum of All Subset XOR Totals](visualizations/1863-sum-of-all-subset-xor-totals.html) | Easy | Bit counting · contribution technique |
| 3513 | [Number of Unique XOR Triplets I](visualizations/3513-number-of-unique-xor-triplets-i.html) | Medium | Bit reasoning · closed form |

---

## Math & number theory
*Euclid, modular arithmetic, base conversion, closed forms. Cheap to learn, and they turn several Hard problems into one-liners.*
**A small toolkit, worth having memorised.**

```python
def gcd(a, b):                       # Euclid, O(log min(a,b))
    while b: a, b = b, a % b
    return a
lcm = a // gcd(a, b) * b             # divide FIRST - avoids overflow
pow(base, exp, MOD)                  # fast modular exponentiation, O(log exp)
pow(a, p - 2, p)                     # modular inverse when p is prime
```

**Index arithmetic** — the three conversions that turn up everywhere:

```python
flat = r * COLS + c                  # flatten   (never * ROWS)
r, c = flat // COLS, flat % COLS     # unflatten
idx  = (idx + k) % total             # wrap - and ALWAYS reduce k % total first
```

**Reduce before you loop.** Any repeated operation with a period collapses: rotations, shifts, cyclic permutations.
`k %= total` is the difference between O(n) and a timeout (1260).

**Enumerate the property, not the range.** When a property is very restrictive and the range is huge, ask *how many
objects satisfy it at all?* There are only 36 sequential-digit numbers in existence (1291). If the count is large
instead, you need digit DP.

**1-based vs 0-based.** Convert at the boundary, do the arithmetic, convert back. That is why bijective base-26
(168) has a `-1` before both the `%` and the `//`, and why circular-array code is full of `((x - 1) % n) + 1`.

**Read constraints as information.** "A permutation of 1..n" means the array carries no information beyond n, and the
answer is a closed form (3513). When the stated brute force is wildly beyond the constraints, the intended solution
is often not a faster search but a proof.

**Traced in this repo** — start with **168, 1071, 3513**:

| # | Problem | Difficulty | The specific idea |
|---|---|---|---|
| 168 | [Excel Sheet Column Title](visualizations/0168-excel-sheet-column-title.html) | Easy | Math · bijective base conversion |
| 628 | [Maximum Product of Three Numbers](visualizations/0628-maximum-product-of-three-numbers.html) | Easy | Sorting · exhaustive case analysis |
| 1071 | [Greatest Common Divisor of Strings](visualizations/1071-greatest-common-divisor-of-strings.html) | Easy | Number theory analogy · gcd on lengths |
| 1260 | [Shift 2D Grid](visualizations/1260-shift-2d-grid.html) | Easy | Flatten · modular shift · unflatten |
| 1344 | [Angle Between Hands of a Clock](visualizations/1344-angle-between-hands-of-a-clock.html) | Medium | Math · modular geometry |
| 1464 | [Maximum Product of Two Elements in an Array](visualizations/1464-maximum-product-of-two-elements-in-an-array.html) | Easy | Single pass · top-k tracking |
| 1929 | [Concatenation of Array](visualizations/1929-concatenation-of-array.html) | Easy | Index arithmetic · pre-sized output |
| 1979 | [Find Greatest Common Divisor of Array](visualizations/1979-find-greatest-common-divisor-of-array.html) | Easy | Number theory · Euclidean algorithm |
| 3221 | [Find the Peaks](visualizations/3221-find-the-peaks.html) | Easy | Array scan · local property |
| 3614 | [Process String With Special Operations II](visualizations/3614-process-string-with-special-operations-ii.html) | Hard | Forward lengths + backward index mapping |
| 3754 | [Concatenate Non-Zero Digits and Multiply by Sum I](visualizations/3754-concatenate-non-zero-digits-and-multiply-by-sum-i.html) | Easy | Digit manipulation · single pass, two accumulators |

---

## Design
*Compose structures: one per required operation, cross-referenced. Map for lookup, list for order, heap for extremes, counter for a running minimum.*
**The method.** List every operation the problem requires, give each one a structure, then work out what pointer
connects them. Almost every "hard" design problem is **a hash map composed with one other structure**.

| Requirement | Structure |
|---|---|
| O(1) lookup by key | hash map |
| O(1) reorder + evict oldest | doubly linked list (map stores **node references**) → **LRU** (146) |
| O(1) random removal | array + map of value → index (380) |
| Evict by frequency, ties by recency | map of frequency → LRU list, + a running minimum → **LFU** (460) |
| Bounded FIFO | ring buffer, or sentinel-bracketed list (622) |
| Time-ordered queries | map of key → sorted list, then binary search (981) |

**Sentinels earn their keep.** Two dummy nodes bracketing a doubly linked list mean every real node has a
predecessor and a successor, so insert and delete are four unconditional assignments with no null checks. The same
idea is a dummy list head, a padded prefix table, and `map[None] = None` in a deep copy.

**The bug that hides.** Every mutation must touch **all** the structures. Removing from the list but not the map
passes small tests and leaks at scale. For each mutation, ask explicitly: *which of my structures does this change?*

**What is actually graded.** Not the code — the trade-offs you volunteer. For anything you build, be ready to state:
average cost, worst case, what triggers the worst case, and memory. Saying those four things unprompted is worth
more than a perfect implementation.

**Traced in this repo** — start with **146, 460**:

| # | Problem | Difficulty | The specific idea |
|---|---|---|---|
| 460 | [LFU Cache](visualizations/0460-lfu-cache.html) | Hard | Design · three maps + per-frequency LRU lists |
| 705 | [Design HashSet](visualizations/0705-design-hashset.html) | Easy | Design · hash table internals |
| 706 | [Design HashMap](visualizations/0706-design-hashmap.html) | Easy | Design · hash table internals |

---

## Sorting & divide and conquer
*T(n) = 2T(n/2) + O(n). Draw the recursion tree once and you own the complexity argument for the whole family.*
**The recurrence.** T(n) = 2T(n/2) + O(n) → O(n log n). Log n levels, O(n) work per level. Draw that picture once and
you own the complexity argument for the entire family.

**Know your sorts by trade-off, not by code.**

| | stable | worst case | extra space |
|---|---|---|---|
| merge | yes | O(n log n) | O(n) |
| quick | no | O(n²) adversarial | O(1) |
| heap | no | O(n log n) | O(1) |
| counting / radix | yes | O(n) — **bounded integer keys only** | O(range) |

Interviewers rarely want you to write one; they want you to pick and justify. And before you reach for `sort()`,
ask two things: *is my sort key a bounded integer?* (→ bucket, 347/1833) and *how much of the order do I actually
need?* (→ one pass for the top two, 1464).

**Combine in a tree, not a chain.** k things to merge? Chain = O(Nk), pairwise tournament = O(N log k), and the code
is barely longer (23). The same applies to concatenating k strings and unioning k sets.

**The merge step is a primitive.** It is LC 21, the inner loop of merge sort, and — with counting added — the way you
count inversions and "smaller elements to the right".

**Traced in this repo** — start with **912, 23**:

| # | Problem | Difficulty | The specific idea |
|---|---|---|---|
| 23 | [Merge k Sorted Lists](visualizations/0023-merge-k-sorted-lists.html) | Hard | Divide and conquer · pairwise merge |
| 703 | [Kth Largest Element in a Stream](visualizations/0703-kth-largest-element-in-a-stream.html) | Easy | Heap · bounded size-k min-heap |
| 912 | [the divide-and-conquer tree](visualizations/0912-sort-an-array.html) | Medium | Divide and conquer · merge sort |

---

## Brute force done right
*Sometimes O(n²) is the intended answer. Make the inner step O(1) and say out loud what you would do if the constraints grew.*
**Sometimes O(n²) is the answer.** Constraints of n ≤ 100 or n ≤ 1000 are the problem *licensing* it. What is being
tested then is whether you write it well.

**Make the inner step O(1).** Carry state as the window grows instead of recomputing it — that is the difference
between O(n²) and O(n³) in 3737, and it is the seed of every sliding-window and prefix-sum optimisation.

**Say what you would do if the constraints grew.** For 3737 the escalation is the ±1 transform plus a Fenwick tree
(3739). For 1967 it is Aho–Corasick. Naming the next rung is worth real credit even when you do not write it.

**Index identity vs value identity.** "Two elements" nearly always means two *positions*, not two *values*. Guard
with `i != j`, not `nums[i] != nums[j]` — this is the same edge case that makes `[3,3]` interesting in Two Sum.

**Know what your library calls cost.** `x in s`, `sorted()`, `str.replace(a, b, 1)`, `heapq.heapify`. For every one
you use, be able to answer "what does that do under the hood, and what is its complexity?"

**Traced in this repo** — start with **3737, 2133**:

| # | Problem | Difficulty | The specific idea |
|---|---|---|---|
| 1967 | [Number of Strings That Appear as Substrings in Word](visualizations/1967-number-of-strings-that-appear-as-substrings-in-word.html) | Easy | String matching · know what your library does |
| 2133 | [Number of Pairs of Strings With Concatenation Equal to Target](visualizations/2133-number-of-pairs-of-strings-with-concatenation-equal-to-target.html) | Medium | Brute force · index vs value identity |
| 3737 | [Count Subarrays With Majority Element I](visualizations/3737-count-subarrays-with-majority-element-i.html) | Medium | Brute force with incremental state |

---

## Eight problems in this repo worth re-reading as pairs

Solving problems in pairs teaches far more than solving twice as many in isolation. Each pair below is the *same*
skeleton with one deliberate difference.

| Pair | The one thing that differs |
|---|---|
| [22](visualizations/0022-generate-parentheses.html) vs [39](visualizations/0039-combination-sum.html) | *when* you can prove a branch is doomed — perfect pruning vs discovering mistakes late |
| [39](visualizations/0039-combination-sum.html) vs [40](visualizations/0040-combination-sum-ii.html) | duplicate suppression, and reuse (`i`) vs single-use (`i+1`) |
| [40](visualizations/0040-combination-sum-ii.html) vs [47](visualizations/0047-permutations-ii.html) | skip duplicate *positions* vs count distinct *values* |
| [217](visualizations/0217-contains-duplicate.html) → [219](visualizations/0219-contains-duplicate-ii.html) → [287](visualizations/0287-find-the-duplicate-number.html) | the same question under three constraint sets: set → window → Floyd |
| [75](visualizations/0075-sort-colors.html) vs [2161](visualizations/2161-partition-array-according-to-given-pivot.html) | one word — *stability* — turns an O(1)-space problem into an O(n)-space one |
| [1833](visualizations/1833-maximum-ice-cream-bars.html) vs [2144](visualizations/2144-minimum-cost-of-buying-candies-with-discount.html) | ascending vs descending, for a nameable reason |
| [2503](visualizations/2503-longest-subarray-with-maximum-bitwise-and.html) vs [934](visualizations/0934-bitwise-ors-of-subarrays.html) | AND clears bits, OR sets them — opposite monotonicity, opposite algorithms |
| [3737](visualizations/3737-count-subarrays-with-majority-element-i.html) vs [3739](visualizations/3739-count-subarrays-with-majority-element-ii.html) | the constraint grows, and the ±1 transform becomes mandatory |
| [3699](visualizations/3699-number-of-zigzag-arrays-i.html) vs [3700](visualizations/3700-number-of-zigzag-arrays-ii.html) | n grows to 10¹⁸, so a linear DP becomes matrix exponentiation |

---

## One habit worth more than the rest

After every problem you solve, write one sentence: **"the reusable capability I just implemented is ______ ."**

Reverse a range in place. Find the middle of a list. Count how many earlier values are smaller. Test whether a
window is valid. Group by a canonical key.

A hundred solved problems is a hundred things to forget. Twenty named capabilities is a toolkit — and hard problems
turn out to be two or three of them composed. That is the difference between recognising a problem you have seen and
solving one you have not.
