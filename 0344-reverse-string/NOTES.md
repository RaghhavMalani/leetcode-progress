# 344. Reverse String
> **Easy** &nbsp;&middot;&nbsp; Two pointers · converging &nbsp;&middot;&nbsp; family: **Two pointers & sliding window**

The smallest possible converging-two-pointer problem. Worth five minutes because the *shape* — start at both ends, swap, step inward — reappears in palindromes, rotations and in-place partitions.

**▶ [Step through this solution line by line](./visualization.html)** — 10 steps, traced on `s = ["h","e","l","l","o"]`.

| | |
|---|---|
| time | O(n) — n/2 swaps |
| space | O(1) — in place, which is the entire point of the problem |

## The idea

Converging pointers in their purest form. The problem is really testing one thing: do you understand that "in place" forbids allocating a second array, and do you know the three-line swap (or Python’s tuple swap) that makes it possible?

## How to recognise it

- Explicit "modify in place / do not return anything / O(1) extra memory".
- The operation is symmetric about the centre — reverse, palindrome check, mirror.
- Anything you can phrase as "pair up element i with element n-1-i".

## Where people go wrong

- **Returning `s[::-1]`.** That allocates a new list and rebinds a local name; the caller’s list is untouched, so the test fails even though the value looks right. `s[:] = s[::-1]` would work but sidesteps the exercise.
- **`while left <= right`.** Harmless (it swaps the middle element with itself) but it signals you have not thought about the invariant.
- **Overwriting before saving.** `s[left] = s[right]; s[right] = s[left]` destroys the value. In Python prefer `s[l], s[r] = s[r], s[l]`, which evaluates the right side first.

## The reusable template

```python
# Converging pointers - reverse / palindrome / mirror
left, right = 0, len(a) - 1
while left < right:
    a[left], a[right] = a[right], a[left]   # or: compare, for palindromes
    left += 1
    right -= 1

# Compose it: rotate an array right by k
#   reverse(a, 0, n-1); reverse(a, 0, k-1); reverse(a, k, n-1)
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Reverse only the vowels | LC 345 — same loop, advance each pointer past non-vowels first. |
| **Valid Palindrome** (LC 125) | Compare instead of swap, and skip non-alphanumerics. |
| Reverse words in a string | LC 151 — reverse the whole thing, then reverse each word. A classic two-stage trick. |
| Rotate array by k | LC 189 — reverse all, reverse the first k, reverse the rest. Same primitive three times. |

## How to think about it next time

Do not skip easy problems like this one — mine them for **primitives**. "Reverse a range in place" is a primitive; once you own it, Rotate Array and Reverse Words become two-line compositions instead of new problems. A good habit: after solving anything easy, ask "what one-sentence operation did I just implement, and what harder problem is built out of it?"

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/reverse-string)
