# 47. Permutations II
> **Medium** &nbsp;&middot;&nbsp; Backtracking · counter as state &nbsp;&middot;&nbsp; family: **Backtracking**

A different weapon for the same job as problem 40. Instead of skipping duplicate *positions*, this counts distinct *values* — so identical numbers are never separate objects to begin with.

**▶ [Step through this solution line by line](./visualization.html)** — 38 steps, traced on `nums = [1,1,2]`.

| | |
|---|---|
| time | O(n! / Πcount[v]! · n) — exactly the number of distinct permutations, times n to copy |
| space | O(n) depth + O(distinct) for the counter |

## The idea

Replacing "which index have I used" with "how many of this value do I have left" is a powerful move. It collapses identical elements into one branch automatically, and it turns the used-set bookkeeping into simple arithmetic. The price is that every choice now has **two** things to undo — the append and the decrement.

## How to recognise it

- Permutations (order matters, all n elements used) with **repeated values** in the input.
- You need *distinct* output rows, and n is small (≤ 8) so factorial work is fine.
- More generally: any time elements are interchangeable, a counter is a better state than a visited-index array.

## Where people go wrong

- **Refunding the count but not popping perm**, or vice versa. The undo must exactly mirror the choose. Write the two lines as a pair, always.
- **Looping over `nums` instead of `count`.** That reintroduces the duplicates you just eliminated — you would visit the 1 at index 0 and the 1 at index 1 as separate branches.
- **Mutating `count` while iterating it** — safe in Python because you only change values, never insert or delete keys. Deleting a key mid-loop would raise.
- **Deduping the final list with a set of tuples.** Correct, but you did all n! work to throw most of it away.

## The reusable template

```python
# Killing duplicate ANSWERS - two interchangeable idioms.

# (a) sort + skip equal neighbours on the SKIP branch   (LC 40, 90)
arr.sort()
path.append(arr[i]); backtrack(i+1); path.pop()
while i+1 < len(arr) and arr[i] == arr[i+1]:
    i += 1
backtrack(i+1)              # skip branch lands on a genuinely NEW value

# (b) loop over distinct VALUES with a count budget     (LC 47)
for val in count:           # keys of the counter, not positions
    if count[val] > 0:
        path.append(val); count[val] -= 1
        backtrack()
        count[val] += 1; path.pop()     # undo BOTH halves
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Input guaranteed distinct | LC 46 — the counter is unnecessary; a visited array or index-swapping is simpler. |
| Combinations with duplicates instead of permutations | LC 40 / 90 — sort and skip equal neighbours. Same goal, different idiom. |
| Next permutation in lexicographic order | LC 31 — an O(n) in-place trick, no recursion. Completely different tool. |
| The k-th permutation directly | LC 60 — factorial number system, O(n²). Do not enumerate. |

## How to think about it next time

Notice what changed between 40 and 47: nothing about the *skeleton*, only the **representation of state**. That is where most of the leverage in backtracking lives. Before you optimise the search, ask whether a better state description makes the problem symmetric-free by construction. "Counts of remaining values" is one of the three or four state representations worth having memorised — the others being "index + accumulator", "bitmask of used items", and "current position in a grid + visited set".

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/permutations-ii)
