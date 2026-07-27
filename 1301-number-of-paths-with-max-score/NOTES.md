# 1301. Number Of Paths With Max Score
> **Hard** &nbsp;·&nbsp; Grid DP &nbsp;·&nbsp; **not solved yet**

There is no solution file in this folder, so there is nothing to trace. When you solve it, the notes below are the starting point.

## Where to start

Two parallel DP tables — best score and how many ways achieve it. Move down/right/diagonal from the bottom-right corner. Read the **Dynamic programming** chapter: the state is (r, c) and the recurrence is a max over three predecessors, with the count summed over whichever predecessors tie.

---

[← all traced solutions](../visualizations/index.html) &nbsp;·&nbsp; [pattern handbook](../PATTERNS.md)
