# 46. Permutations
> **Medium** &nbsp;·&nbsp; Recursion · bottom-up construction (NOT backtracking) &nbsp;·&nbsp; family: **Backtracking**

Your solution here is correct but it is *not* backtracking — there is no shared mutable state and no undo step. Worth understanding as a contrast, and worth re-solving with the standard skeleton so the pattern transfers to 47, 39 and N-Queens.

**▶ [Step through this solution line by line](../visualizations/0046-permutations.html)** — 29 steps, traced on `nums = [1,2,3]`.

| | |
|---|---|
| time | O(n! · n²) — n! results, and each insert copies an O(n) list, n+1 times per level |
| space | O(n! · n) to hold all the intermediate lists — noticeably worse than backtracking |

## The idea

Two legitimate ways to generate every permutation. **Bottom-up (this code):** get all permutations of the tail, then splice the head into every gap. No shared state, purely functional, easy to reason about. **Backtracking:** one shared list, choose / explore / un-choose. Backtracking uses O(n) extra space instead of O(n!·n) and is the one every follow-up question is phrased in terms of.

## How to recognise it

- "All permutations", "all orderings", "all arrangements", n ≤ 8ish.
- If the input can repeat, you need the counter idiom → LC 47.
- If you need only the k-th permutation, or the *next* one, do not enumerate — LC 60 and LC 31 have direct O(n) / O(n²) constructions.

## Where people go wrong

- **The one this code gets right:** `p_copy = p.copy()` on line 11. Insert into `p` itself and every subsequent gap builds on the corrupted list.
- **Returning `[]` instead of `[[]]` at the base case.** The empty list means "no permutations exist"; `[[]]` means "exactly one permutation, the empty one". Return the wrong one and the whole recursion collapses to nothing — a very common and very confusing bug.
- **Slicing `nums[1:]` at every level** costs O(n) per call and quietly adds a factor to the runtime. Fine at n ≤ 8; worth mentioning aloud.

## The reusable template

```python
# The version to have in your fingers - same problem, backtracking form.
def permute(nums):
    res, perm = [], []
    used = [False] * len(nums)

    def dfs():
        if len(perm) == len(nums):
            res.append(perm.copy())
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True;  perm.append(nums[i])    # choose
            dfs()                                    # explore
            perm.pop();      used[i] = False         # un-choose

    dfs()
    return res
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Input contains duplicates | LC 47 — counter budget, or sort + skip. |
| Permutations of a fixed length k | Backtracking with a depth guard; bottom-up does not adapt cleanly. |
| **N-Queens** (LC 51) | A permutation search with pruning. Only the backtracking form supports pruning at all — you cannot abandon a branch you have already fully built. |
| Next permutation | LC 31 — O(n) in place, no recursion. |

## How to think about it next time

Here is the concrete reason to re-solve this with backtracking: **bottom-up construction cannot prune.** It builds every complete answer and only then filters. The moment a problem adds a constraint — no two queens attacking, sum must equal X, string must stay valid — you need to abandon partial answers early, and that requires the shared-state-plus-undo shape. Your 47 solution already uses it. Rewrite 46 in the same style, diff the two files, and the pattern is yours.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/permutations)
