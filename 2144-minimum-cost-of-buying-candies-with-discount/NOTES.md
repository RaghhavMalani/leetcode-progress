# 2144. Minimum Cost of Buying Candies With Discount
> **Easy** &nbsp;&middot;&nbsp; Greedy · sort descending, take every third &nbsp;&middot;&nbsp; family: **Greedy**

Two lines once you see it: sort descending and skip index 2, 5, 8, …. The direction of the sort is the whole decision, and it follows from wanting the *free* items to be expensive.

**▶ [Step through this solution line by line](./visualization.html)** — 9 steps, traced on `cost = [6,5,7,9,2,2]`.

| | |
|---|---|
| time | O(n log n) — the sort |
| space | O(1) |

## The idea

Minimising what you pay is the same as **maximising what you get free**. The offer constrains the free candy to be no more expensive than the two purchased, so in sorted-descending order the best free candy in each group of three is the third. Grouping the largest values together and freeing the third of each group is optimal by an exchange argument: swapping any free candy for a more expensive one that is still legal never increases the cost.

## How to recognise it

- "Buy k, get one free" offers, bulk discounts, or any rule that lets you skip elements subject to a size condition.
- The direction of the sort is decided by **which side of the trade you want to be large**. Free items → sort descending. Paid items minimised → same thing, but it is clearer to reason about the free ones.
- Compare with LC 1833 in your repo: there you maximise the COUNT under a budget, so you sort ascending. Same family, opposite direction, for a nameable reason.

## Where people go wrong

- **Sorting ascending.** Then the free candies are the cheap ones and you pay far more. This is the entire trap.
- **Using `i % 3 == 0`.** Off by two — with 0-based indexing the third element of a group is at 0, 1, **2**.
- **Handling a leftover group specially.** Groups of one or two at the end have no free candy, and `i % 3 != 2` handles that automatically.
- **Not justifying the greedy.** One sentence: the free item must be the cheapest of its trio, so make the trios out of consecutive descending values.

## The reusable template

```python
# minimise what you PAY == maximise what you get FREE
cost.sort(reverse=True)                 # descending: free items should be pricey
return sum(c for i, c in enumerate(cost) if i % 3 != 2)

# buy k get one free ->  i % (k + 1) != k
# contrast LC 1833: maximise COUNT under a budget -> sort ASCENDING
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Buy k, get one free | `i % (k+1) != k`. |
| **Maximum Ice Cream Bars** (LC 1833) | Maximise count under a budget → sort ASCENDING. Also in your repo. |
| Free item may be any cheaper item, not just within the trio | Same answer — the grouping already respects that constraint. |
| Percentage discount on the cheapest | A different objective; re-derive which items you want cheap. |

## How to think about it next time

For any discount or skip-based greedy, write down the objective as "**maximise the total value of the things I do not pay for**" and then ask what the rules allow you to skip. That reframing decides the sort direction immediately, and it is the same reasoning that tells you to sort ascending in LC 1833 and descending here. Two nearly identical problems, opposite sorts, one question that distinguishes them.

---

[← all traced solutions](../visualizations/index.html) &nbsp;&middot;&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;&middot;&nbsp; [on LeetCode](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount)
