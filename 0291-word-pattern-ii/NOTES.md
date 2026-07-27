# 291. Word Pattern II
> **Medium** &nbsp;·&nbsp; Backtracking · bijection search &nbsp;·&nbsp; family: **Backtracking**

Backtracking where the mutable state is a *dictionary*, not a list. Same three beats — bind, explore, unbind — but there are two structures to undo and both matter.

**▶ [Step through this solution line by line](../visualizations/0291-word-pattern-ii.html)** — 27 steps, traced on `pattern = "aba", s = "aabba"`.

| | |
|---|---|
| time | O(C(n-1, m-1) · n) — the ways to cut s into m pieces, times the cost of comparisons |
| space | O(m + n) for mapping, used, and the recursion depth |

## The idea

The state being mutated does not have to be a list. Here it is a `dict` plus a `set`, and the undo is `del mapping[ch]` plus `used.remove(candidate)`. Keeping **both** structures in sync is the whole difficulty: `mapping` enforces "one letter means one word", `used` enforces the other direction, "one word is meant by one letter".

## How to recognise it

- You must find a **consistent assignment** and the assignment is not forced — you have to guess and revise.
- The word "bijection" or a rule like "no two characters map to the same string".
- A string that must be **cut into pieces** at unknown positions. The `for end in range(j+1, len(s)+1)` loop is the canonical "try every cut point" idiom.

## Where people go wrong

- **Only tracking `mapping`.** Then "a"→"x" and "b"→"x" both pass and you accept patterns you should reject. The `used` set is not optional.
- **Undoing only one of the two.** Delete from `mapping` but leave the word in `used` and it stays permanently claimed — later branches mysteriously fail.
- **Undoing after a success.** Notice line 33 returns *before* the deletes. That is deliberate: on success you keep the binding, on failure you roll it back.
- **Empty-word candidates.** The range starts at `j+1`, not `j`, so every candidate is at least one character. Allow the empty string and you get infinite recursion.

## The reusable template

```python
# "Try every cut point" - the loop behind Word Break, Palindrome
# Partitioning, Restore IP Addresses, and this problem.

def dfs(j):                       # j = how much of s is consumed
    if j == len(s):
        return True               # or: res.append(path.copy())
    for end in range(j + 1, len(s) + 1):
        piece = s[j:end]
        if not ok(piece):         # the ONLY problem-specific line
            continue
        path.append(piece)        # choose
        if dfs(end):              # explore
            return True
        path.pop()                # un-choose
    return False
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Words are pre-split by spaces | LC 290 Word Pattern — no search at all, one linear pass with two dicts. The cut points being unknown is the entire difficulty here. |
| **Word Break** (LC 139) | Same "try every cut point" loop, but with a fixed dictionary and memoisation instead of a bijection. |
| **Palindrome Partitioning** (LC 131) | Identical cut-point loop, guard is `is_palindrome(s[j:end])`. |
| **Restore IP Addresses** (LC 93) | The same loop, capped at 3 characters and 4 pieces. |

## How to think about it next time

Two transferable ideas live in this problem. First: **"try every cut point" is a loop, not a mystery** — `for end in range(j+1, len(s)+1)`, recurse on `end`. Once you see it, Word Break, Palindrome Partitioning and Restore IP Addresses are the same code with a different guard. Second: **the undo must exactly mirror the choose, line for line**. Write the choose lines and the undo lines as a visual block, and count them — if you added two things and removed one, you have a bug you will spend an hour finding.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/word-pattern-ii)
