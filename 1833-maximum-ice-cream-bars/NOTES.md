# 1833. Maximum Ice Cream Bars
> **Medium** &nbsp;·&nbsp; Greedy · counting sort &nbsp;·&nbsp; family: **Greedy**

Buy cheapest first — but the interesting choice here is counting sort instead of `sort()`, which turns O(n log n) into O(n + maxPrice).

**▶ [Step through this solution line by line](../visualizations/1833-maximum-ice-cream-bars.html)** — 16 steps, traced on `costs = [1,3,2,4,1], coins = 7`.

| | |
|---|---|
| time | O(n + maxPrice) — linear when prices are bounded |
| space | O(maxPrice) |

## The idea

Two separate ideas. **The greedy:** to maximise the *count* of items under a budget, always take the cheapest — proved by an exchange argument. **The sort:** when the sort key is a bounded integer, counting sort beats comparison sort, exactly as in LC 347 in your repo.

## How to recognise it

- "Maximum number of items within a budget", all items otherwise identical. If items had different *values*, this would be knapsack and greedy would fail.
- Bounded integer keys (prices ≤ 10⁵) → counting sort is available.
- The greedy dies the moment items have differing value-per-cost — that is the line between this and 0/1 knapsack.

## Where people go wrong

- **Buying one bar at a time in a loop.** Correct but O(coins) in the worst case; `coins // price` buys the whole tier at once.
- **Allocating 100001 slots regardless of input size.** Fine here, but if maxPrice were 10⁹ the counting sort would be worse than sorting. Check the bound before choosing.
- **Assuming greedy always works for budget problems.** It works only because all bars are worth exactly 1. Say that.
- **Not stopping early.** Once coins run out you can break — a small win, and it shows you noticed prices are ascending.

## The reusable template

```python
# greedy (cheapest first) + counting sort instead of sort()
freq = [0] * (MAX_PRICE + 1)
for c in costs:
    freq[c] += 1

ans = 0
for price in range(1, MAX_PRICE + 1):
    if not freq[price]:
        continue
    buy = min(freq[price], coins // price)   # whole tier at once, not one by one
    ans   += buy
    coins -= buy * price
    if coins < price:
        break                                # prices only rise from here
return ans
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| Items have different values | 0/1 knapsack DP. Greedy is wrong. |
| Fractional purchases allowed | Fractional knapsack — greedy by value/weight ratio is optimal. |
| **Minimum Cost of Buying Candies** (LC 2144) | Sort DESCENDING and skip every third. Also in your repo. |
| Unbounded quantities per price | Buy as many of the cheapest as the budget allows; one line. |

## How to think about it next time

Two questions to keep separate. **(1) Is the greedy correct?** Answer it with an exchange argument, not intuition. **(2) What is the cheapest way to get the order I need?** Sorting is the default, but bounded integer keys open the door to counting sort. Most people conflate these and either use a greedy they cannot justify or reach for `sort()` reflexively.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/maximum-ice-cream-bars)
