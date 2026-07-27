# 122. Best Time to Buy and Sell Stock II
> **Medium** &nbsp;·&nbsp; Greedy · decompose into local gains &nbsp;·&nbsp; family: **Greedy**

Four lines, and the whole difficulty is proving they are right. The argument: a hold from day a to day b earns exactly the sum of the daily changes between them, so taking every positive change is optimal and no worse.

**▶ [Step through this solution line by line](../visualizations/0122-best-time-to-buy-and-sell-stock-ii.html)** — 12 steps, traced on `prices = [7,1,5,3,6,4]`.

| | |
|---|---|
| time | O(n) |
| space | O(1) |

## The idea

A **telescoping** argument. prices[b] − prices[a] = Σ (prices[i] − prices[i−1]) for i in (a, b]. So any strategy’s profit is a sum of daily deltas, and the best possible sum of a subset of deltas is simply all the positive ones. Being able to give that two-line proof is what separates a greedy answer from a lucky guess.

## How to recognise it

- Unlimited transactions with no cooldown and no fee — those extra rules are exactly what breaks the greedy and forces DP.
- A global optimum that decomposes into independent local choices. If choices interact, greedy fails.
- The tell that greedy is *wrong*: a constraint linking decisions ("at most k transactions", "wait a day after selling").

## Where people go wrong

- **Reaching for DP.** It works, it is O(n) too, and it is far more code. Recognising the greedy is the point.
- **Tracking a buy price and a sell price.** Correct but noisier; the delta formulation removes the state entirely.
- **Applying this to LC 121.** Only *one* transaction is allowed there, so this over-counts badly. Check the transaction limit before you write a line.
- **Not being able to justify it.** "It just works" is the wrong answer; the telescoping argument takes ten seconds.

## The reusable template

```python
# Greedy by telescoping - take every positive daily delta
profit = 0
for i in range(1, len(prices)):
    if prices[i] > prices[i - 1]:
        profit += prices[i] - prices[i - 1]
return profit

# WHY: prices[b] - prices[a] == sum of the daily deltas in (a, b].
# So every strategy's profit is a subset-sum of deltas, and the best
# subset is "all the positive ones". Add a fee or a cooldown and this
# argument collapses -> use DP.
```

## If the interviewer twists it

| Variant | What changes |
|---|---|
| **At most one** transaction (LC 121) | Track the minimum price so far and the best profit against it. |
| **At most k** transactions (LC 188) | DP over (day, transactions used, holding or not). Greedy dies. |
| With a transaction fee (LC 714) | Greedy dies — the fee makes tiny gains unprofitable. Two-state DP. |
| With a cooldown (LC 309) | Three-state DP: holding, just sold, free. |

## How to think about it next time

The habit worth building is: **when a greedy solution occurs to you, spend thirty seconds trying to prove it before you write it.** Usually the proof is either an exchange argument ("swapping to the greedy choice never makes things worse") or a decomposition like this one. If you cannot construct either, treat the greedy as suspect and reach for DP. Interviewers grade greedy answers on the justification far more than on the code, because the code is always four lines.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md) &nbsp;·&nbsp; [problem on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii)
