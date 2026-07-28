# 42. Trapping Rain Water
> **Hard** &nbsp;&middot;&nbsp; Two pointers · converging &nbsp;&middot;&nbsp; family: **Two pointers & sliding window**

The classic argument for why two pointers work: you do not need both maxima, only to know which one is smaller — and comparing the two heights tells you that for free.

**▶ [Step through this solution line by line](./visualization.html)** — 46 steps, traced on `height = [0,1,0,2,1,0,1,3,2,1,2,1]`.

| | |
|---|---|
| time | O(n) — single pass |
| space | O(1) — beats the prefix-max arrays and the stack solution |

## The idea

Water above column i is `min(maxLeft[i], maxRight[i]) - height[i]`. The naive route precomputes both arrays in O(n) space. The two-pointer trick: whichever of `height[left]` and `height[right]` is **smaller** is the side whose maximum is binding, and you can settle that column immediately — you never need the far side’s exact value, only the guarantee that it is at least as big.

## How to recognise it

- An array where the answer at each index depends on something to the **left and to the right** of it.
- You have a formula involving `min(prefix_max, suffix_max)`. That shape is almost always convertible from two arrays to two pointers.
- The interviewer asks for O(1) space after you give the O(n) prefix/suffix answer — this is that follow-up.

## Where people go wrong

- **Comparing `left_max` with `right_max` instead of `height[left]` with `height[right]`.** Both are workable formulations, but mixing them breaks the invariant. Pick one and be consistent.
- **Updating the max after computing the water.** Then a wall column reports negative water. The `>=` branch must come first.
- **`while left <= right`.** When they meet, that column is the global maximum and traps nothing; including it is harmless here but the strict `<` is the honest invariant.
- **Reaching for the monotonic stack** because you have seen it done that way. The stack solution is O(n) time and O(n) space and considerably harder to get right under pressure. Give this one first, mention the stack as an alternative.

## The reusable template

```python
# Converging two pointers - the general shape
left, right = 0, len(a) - 1
while left < right:
    if <the left side is currently the binding constraint>:
        ...settle index `left`...
        left += 1
    else:
        ...settle index `right`...
        right -= 1

# The pattern is valid only when you can PROVE that the side you move
# can be finalised now and never needs revisiting. Say that proof out
# loud in an interview - it is what is actually being tested.
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **Container With Most Water** (LC 11) | Same converging pointers, different rule: move whichever wall is shorter, because only it limits the area. |
| Trapping Rain Water **II** (LC 407) | 2D. Pointers do not generalise — you need a min-heap flooding from the border inwards. |
| Prefix/suffix max arrays | The O(n)-space version. Simpler to derive, and the right first answer to state before optimising. |
| Monotonic stack | Computes water layer by horizontal layer. Worth knowing because that same stack solves LC 84 and LC 739. |

## How to think about it next time

The generalisable move here is: **when the answer needs two pieces of information and you only need to know which is smaller, you can often replace precomputation with a moving pointer.** Ask yourself, at each step, "which side is currently the bottleneck, and can I finalise it right now?" If the answer is yes, converging pointers apply. Container With Most Water is the same question with a different bottleneck, which is why the two problems feel identical once you have seen this argument.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/trapping-rain-water)
