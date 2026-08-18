<!-- TRACED-VISUALIZATIONS:START -->
## 📊 Traced solutions & pattern handbook

Every solution in this repo has been replayed **line by line** against its own source, with the data structures
drawn as they change — the recursion tree growing and pruning, the sliding window expanding, the pointers moving,
the heap reordering.

| | |
|---|---|
| **[Open the Dojo](visualizations/dojo.html)** | active recall: name the pattern from a cold statement, predict the next step, rebuild your code from shuffled lines, rebuild the 16 skeletons, or sit a timed 45-minute interview. Spaced repetition, mastery map, and it tracks *which kind* of mistake you keep making. |
| **[Traced solutions](visualizations/index.html)** | every solution replayed line by line, with the data structures drawn as they change |
| **[Pattern handbook](PATTERNS.md)** | 16 families: recognition signals, templates, pitfalls, how to think about each |
| **[Study plan](STUDY-PLAN.md)** | the next 30 problems, aimed at the families that are measurably thin |
| **[Refactor queue](REFACTOR.md)** | 12 accepted solutions worth rewriting, ranked, with the reason |
| `NOTES.md` + `visualization.html` in each problem folder | the trace and the theory, right next to the code |

### Keeping it up to date

Solve something new on LeetCode, then **double-click `sync.bat`** (or run `python sync.py`). It pulls your new
commits, runs each new solution under `sys.settrace` to build its trace automatically, writes its notes, and
rebuilds the index and the Dojo. No configuration — inputs come from the problem's own README.

```
python sync.py            # pull, trace anything new, rebuild
python sync.py --dry      # show what it would do
python visualizations/trace.py 0078-subsets --input "nums=[1,2,3,4]"   # trace any input you like
```

Works on a phone. Everything is static HTML — no server, no build step, no network.

Open a page and use **← →** to step, **space** to play, or drag the scrubber. Each page ends with recognition
signals, a template, pitfalls, interviewer variants, and complexity.

<!-- TRACED-VISUALIZATIONS:END -->

# leetcode-progress
A collection of LeetCode questions to ace the coding interview! - Created using [LeetHub v2](https://github.com/arunbhardwaj/LeetHub-2.0)

<!---LeetCode Topics Start-->
# LeetCode Topics
## Array
|  |
| ------- |
| [0001-two-sum](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0001-two-sum) |
| [0014-longest-common-prefix](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0014-longest-common-prefix) |
| [0036-valid-sudoku](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0036-valid-sudoku) |
| [0039-combination-sum](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0039-combination-sum) |
| [0040-combination-sum-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0040-combination-sum-ii) |
| [0042-trapping-rain-water](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0042-trapping-rain-water) |
| [0046-permutations](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0046-permutations) |
| [0047-permutations-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0047-permutations-ii) |
| [0049-group-anagrams](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0049-group-anagrams) |
| [0057-insert-interval](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0057-insert-interval) |
| [0075-sort-colors](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0075-sort-colors) |
| [0078-subsets](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0078-subsets) |
| [0079-word-search](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0079-word-search) |
| [0081-search-in-rotated-sorted-array-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0081-search-in-rotated-sorted-array-ii) |
| [0090-subsets-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0090-subsets-ii) |
| [0122-best-time-to-buy-and-sell-stock-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0122-best-time-to-buy-and-sell-stock-ii) |
| [0128-longest-consecutive-sequence](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0128-longest-consecutive-sequence) |
| [0130-surrounded-regions](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0130-surrounded-regions) |
| [0136-single-number](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0136-single-number) |
| [0200-number-of-islands](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0200-number-of-islands) |
| [0217-contains-duplicate](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0217-contains-duplicate) |
| [0219-contains-duplicate-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0219-contains-duplicate-ii) |
| [0238-product-of-array-except-self](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0238-product-of-array-except-self) |
| [0269-alien-dictionary](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0269-alien-dictionary) |
| [0287-find-the-duplicate-number](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0287-find-the-duplicate-number) |
| [0304-range-sum-query-2d-immutable](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0304-range-sum-query-2d-immutable) |
| [0347-top-k-frequent-elements](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0347-top-k-frequent-elements) |
| [0463-island-perimeter](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0463-island-perimeter) |
| [0542-01-matrix](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0542-01-matrix) |
| [0622-design-circular-queue](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0622-design-circular-queue) |
| [0628-maximum-product-of-three-numbers](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0628-maximum-product-of-three-numbers) |
| [0682-baseball-game](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0682-baseball-game) |
| [0694-number-of-distinct-islands](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0694-number-of-distinct-islands) |
| [0704-binary-search](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0704-binary-search) |
| [0705-design-hashset](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0705-design-hashset) |
| [0706-design-hashmap](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0706-design-hashmap) |
| [0733-flood-fill](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0733-flood-fill) |
| [0739-daily-temperatures](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0739-daily-temperatures) |
| [0741-cherry-pickup](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0741-cherry-pickup) |
| [0773-sliding-puzzle](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0773-sliding-puzzle) |
| [0860-lemonade-change](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0860-lemonade-change) |
| [0877-stone-game](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0877-stone-game) |
| [0912-sort-an-array](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0912-sort-an-array) |
| [0934-bitwise-ors-of-subarrays](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0934-bitwise-ors-of-subarrays) |
| [0994-rotting-oranges](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0994-rotting-oranges) |
| [1020-number-of-enclaves](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1020-number-of-enclaves) |
| [1199-minimum-time-to-build-blocks](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1199-minimum-time-to-build-blocks) |
| [1288-remove-covered-intervals](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1288-remove-covered-intervals) |
| [1406-stone-game-iii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1406-stone-game-iii) |
| [1464-maximum-product-of-two-elements-in-an-array](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1464-maximum-product-of-two-elements-in-an-array) |
| [1631-path-with-minimum-effort](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1631-path-with-minimum-effort) |
| [1732-find-the-highest-altitude](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1732-find-the-highest-altitude) |
| [1833-maximum-ice-cream-bars](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1833-maximum-ice-cream-bars) |
| [1840-maximum-building-height](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1840-maximum-building-height) |
| [1846-maximum-element-after-decreasing-and-rearranging](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1846-maximum-element-after-decreasing-and-rearranging) |
| [1858-longest-word-with-all-prefixes](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1858-longest-word-with-all-prefixes) |
| [1863-sum-of-all-subset-xor-totals](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1863-sum-of-all-subset-xor-totals) |
| [1929-concatenation-of-array](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1929-concatenation-of-array) |
| [1967-number-of-strings-that-appear-as-substrings-in-word](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1967-number-of-strings-that-appear-as-substrings-in-word) |
| [1979-find-greatest-common-divisor-of-array](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1979-find-greatest-common-divisor-of-array) |
| [2133-number-of-pairs-of-strings-with-concatenation-equal-to-target](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2133-number-of-pairs-of-strings-with-concatenation-equal-to-target) |
| [2144-minimum-cost-of-buying-candies-with-discount](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2144-minimum-cost-of-buying-candies-with-discount) |
| [2196-create-binary-tree-from-descriptions](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2196-create-binary-tree-from-descriptions) |
| [2450-minimum-replacements-to-sort-the-array](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2450-minimum-replacements-to-sort-the-array) |
| [2503-longest-subarray-with-maximum-bitwise-and](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2503-longest-subarray-with-maximum-bitwise-and) |
| [2574-left-and-right-sum-differences](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2574-left-and-right-sum-differences) |
| [2812-find-the-safest-path-in-a-grid](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2812-find-the-safest-path-in-a-grid) |
| [2958-length-of-longest-subarray-with-at-most-k-frequency](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2958-length-of-longest-subarray-with-at-most-k-frequency) |
| [3020-find-the-maximum-number-of-elements-in-subset](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3020-find-the-maximum-number-of-elements-in-subset) |
| [3221-find-the-peaks](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3221-find-the-peaks) |
| [3336-find-the-number-of-subsequences-with-equal-gcd](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3336-find-the-number-of-subsequences-with-equal-gcd) |
| [3471-find-the-largest-almost-missing-integer](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3471-find-the-largest-almost-missing-integer) |
| [3513-number-of-unique-xor-triplets-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3513-number-of-unique-xor-triplets-i) |
| [3532-path-existence-queries-in-a-graph-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3532-path-existence-queries-in-a-graph-i) |
| [3534-path-existence-queries-in-a-graph-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3534-path-existence-queries-in-a-graph-ii) |
| [3559-number-of-ways-to-assign-edge-weights-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3559-number-of-ways-to-assign-edge-weights-ii) |
| [3620-network-recovery-pathways](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3620-network-recovery-pathways) |
| [3689-maximum-total-subarray-value-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3689-maximum-total-subarray-value-i) |
| [3702-longest-subsequence-with-non-zero-bitwise-xor](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3702-longest-subsequence-with-non-zero-bitwise-xor) |
| [3731-find-missing-elements](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3731-find-missing-elements) |
| [3737-count-subarrays-with-majority-element-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3737-count-subarrays-with-majority-element-i) |
| [3739-count-subarrays-with-majority-element-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3739-count-subarrays-with-majority-element-ii) |
## Hash Table
|  |
| ------- |
| [0001-two-sum](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0001-two-sum) |
| [0003-longest-substring-without-repeating-characters](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0003-longest-substring-without-repeating-characters) |
| [0017-letter-combinations-of-a-phone-number](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0017-letter-combinations-of-a-phone-number) |
| [0036-valid-sudoku](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0036-valid-sudoku) |
| [0049-group-anagrams](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0049-group-anagrams) |
| [0126-word-ladder-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0126-word-ladder-ii) |
| [0127-word-ladder](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0127-word-ladder) |
| [0128-longest-consecutive-sequence](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0128-longest-consecutive-sequence) |
| [0138-copy-list-with-random-pointer](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0138-copy-list-with-random-pointer) |
| [0141-linked-list-cycle](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0141-linked-list-cycle) |
| [0146-lru-cache](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0146-lru-cache) |
| [0217-contains-duplicate](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0217-contains-duplicate) |
| [0219-contains-duplicate-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0219-contains-duplicate-ii) |
| [0242-valid-anagram](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0242-valid-anagram) |
| [0291-word-pattern-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0291-word-pattern-ii) |
| [0347-top-k-frequent-elements](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0347-top-k-frequent-elements) |
| [0387-first-unique-character-in-a-string](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0387-first-unique-character-in-a-string) |
| [0460-lfu-cache](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0460-lfu-cache) |
| [0694-number-of-distinct-islands](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0694-number-of-distinct-islands) |
| [0705-design-hashset](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0705-design-hashset) |
| [0706-design-hashmap](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0706-design-hashmap) |
| [1079-letter-tile-possibilities](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1079-letter-tile-possibilities) |
| [1358-number-of-substrings-containing-all-three-characters](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1358-number-of-substrings-containing-all-three-characters) |
| [2133-number-of-pairs-of-strings-with-concatenation-equal-to-target](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2133-number-of-pairs-of-strings-with-concatenation-equal-to-target) |
| [2196-create-binary-tree-from-descriptions](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2196-create-binary-tree-from-descriptions) |
| [2958-length-of-longest-subarray-with-at-most-k-frequency](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2958-length-of-longest-subarray-with-at-most-k-frequency) |
| [3016-minimum-number-of-pushes-to-type-word-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3016-minimum-number-of-pushes-to-type-word-ii) |
| [3020-find-the-maximum-number-of-elements-in-subset](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3020-find-the-maximum-number-of-elements-in-subset) |
| [3471-find-the-largest-almost-missing-integer](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3471-find-the-largest-almost-missing-integer) |
| [3532-path-existence-queries-in-a-graph-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3532-path-existence-queries-in-a-graph-i) |
| [3731-find-missing-elements](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3731-find-missing-elements) |
| [3737-count-subarrays-with-majority-element-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3737-count-subarrays-with-majority-element-i) |
| [3739-count-subarrays-with-majority-element-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3739-count-subarrays-with-majority-element-ii) |
## Matrix
|  |
| ------- |
| [0036-valid-sudoku](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0036-valid-sudoku) |
| [0079-word-search](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0079-word-search) |
| [0130-surrounded-regions](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0130-surrounded-regions) |
| [0200-number-of-islands](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0200-number-of-islands) |
| [0304-range-sum-query-2d-immutable](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0304-range-sum-query-2d-immutable) |
| [0463-island-perimeter](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0463-island-perimeter) |
| [0542-01-matrix](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0542-01-matrix) |
| [0694-number-of-distinct-islands](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0694-number-of-distinct-islands) |
| [0733-flood-fill](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0733-flood-fill) |
| [0741-cherry-pickup](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0741-cherry-pickup) |
| [0773-sliding-puzzle](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0773-sliding-puzzle) |
| [0994-rotting-oranges](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0994-rotting-oranges) |
| [1020-number-of-enclaves](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1020-number-of-enclaves) |
| [1631-path-with-minimum-effort](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1631-path-with-minimum-effort) |
| [2812-find-the-safest-path-in-a-grid](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2812-find-the-safest-path-in-a-grid) |
## Sorting
|  |
| ------- |
| [0047-permutations-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0047-permutations-ii) |
| [0049-group-anagrams](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0049-group-anagrams) |
| [0075-sort-colors](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0075-sort-colors) |
| [0217-contains-duplicate](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0217-contains-duplicate) |
| [0242-valid-anagram](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0242-valid-anagram) |
| [0347-top-k-frequent-elements](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0347-top-k-frequent-elements) |
| [0628-maximum-product-of-three-numbers](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0628-maximum-product-of-three-numbers) |
| [0694-number-of-distinct-islands](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0694-number-of-distinct-islands) |
| [0912-sort-an-array](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0912-sort-an-array) |
| [1288-remove-covered-intervals](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1288-remove-covered-intervals) |
| [1464-maximum-product-of-two-elements-in-an-array](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1464-maximum-product-of-two-elements-in-an-array) |
| [1833-maximum-ice-cream-bars](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1833-maximum-ice-cream-bars) |
| [1840-maximum-building-height](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1840-maximum-building-height) |
| [1846-maximum-element-after-decreasing-and-rearranging](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1846-maximum-element-after-decreasing-and-rearranging) |
| [2144-minimum-cost-of-buying-candies-with-discount](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2144-minimum-cost-of-buying-candies-with-discount) |
| [3016-minimum-number-of-pushes-to-type-word-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3016-minimum-number-of-pushes-to-type-word-ii) |
| [3534-path-existence-queries-in-a-graph-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3534-path-existence-queries-in-a-graph-ii) |
| [3731-find-missing-elements](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3731-find-missing-elements) |
## String
|  |
| ------- |
| [0003-longest-substring-without-repeating-characters](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0003-longest-substring-without-repeating-characters) |
| [0014-longest-common-prefix](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0014-longest-common-prefix) |
| [0017-letter-combinations-of-a-phone-number](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0017-letter-combinations-of-a-phone-number) |
| [0022-generate-parentheses](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0022-generate-parentheses) |
| [0049-group-anagrams](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0049-group-anagrams) |
| [0079-word-search](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0079-word-search) |
| [0093-restore-ip-addresses](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0093-restore-ip-addresses) |
| [0126-word-ladder-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0126-word-ladder-ii) |
| [0127-word-ladder](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0127-word-ladder) |
| [0131-palindrome-partitioning](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0131-palindrome-partitioning) |
| [0168-excel-sheet-column-title](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0168-excel-sheet-column-title) |
| [0242-valid-anagram](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0242-valid-anagram) |
| [0269-alien-dictionary](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0269-alien-dictionary) |
| [0291-word-pattern-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0291-word-pattern-ii) |
| [0344-reverse-string](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0344-reverse-string) |
| [0387-first-unique-character-in-a-string](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0387-first-unique-character-in-a-string) |
| [1071-greatest-common-divisor-of-strings](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1071-greatest-common-divisor-of-strings) |
| [1079-letter-tile-possibilities](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1079-letter-tile-possibilities) |
| [1081-smallest-subsequence-of-distinct-characters](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1081-smallest-subsequence-of-distinct-characters) |
| [1358-number-of-substrings-containing-all-three-characters](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1358-number-of-substrings-containing-all-three-characters) |
| [1858-longest-word-with-all-prefixes](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1858-longest-word-with-all-prefixes) |
| [1967-number-of-strings-that-appear-as-substrings-in-word](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1967-number-of-strings-that-appear-as-substrings-in-word) |
| [2133-number-of-pairs-of-strings-with-concatenation-equal-to-target](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2133-number-of-pairs-of-strings-with-concatenation-equal-to-target) |
| [3014-minimum-number-of-pushes-to-type-word-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3014-minimum-number-of-pushes-to-type-word-i) |
| [3016-minimum-number-of-pushes-to-type-word-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3016-minimum-number-of-pushes-to-type-word-ii) |
| [3348-smallest-divisible-digit-product-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3348-smallest-divisible-digit-product-ii) |
| [3499-maximize-active-section-with-trade-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3499-maximize-active-section-with-trade-i) |
| [3614-process-string-with-special-operations-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3614-process-string-with-special-operations-ii) |
## Divide and Conquer
|  |
| ------- |
| [0023-merge-k-sorted-lists](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0023-merge-k-sorted-lists) |
| [0347-top-k-frequent-elements](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0347-top-k-frequent-elements) |
| [0912-sort-an-array](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0912-sort-an-array) |
| [3737-count-subarrays-with-majority-element-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3737-count-subarrays-with-majority-element-i) |
| [3739-count-subarrays-with-majority-element-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3739-count-subarrays-with-majority-element-ii) |
## Heap (Priority Queue)
|  |
| ------- |
| [0023-merge-k-sorted-lists](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0023-merge-k-sorted-lists) |
| [0347-top-k-frequent-elements](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0347-top-k-frequent-elements) |
| [0703-kth-largest-element-in-a-stream](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0703-kth-largest-element-in-a-stream) |
| [0912-sort-an-array](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0912-sort-an-array) |
| [1199-minimum-time-to-build-blocks](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1199-minimum-time-to-build-blocks) |
| [1464-maximum-product-of-two-elements-in-an-array](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1464-maximum-product-of-two-elements-in-an-array) |
| [1631-path-with-minimum-effort](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1631-path-with-minimum-effort) |
| [2812-find-the-safest-path-in-a-grid](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2812-find-the-safest-path-in-a-grid) |
| [3620-network-recovery-pathways](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3620-network-recovery-pathways) |
## Bucket Sort
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0347-top-k-frequent-elements) |
| [0912-sort-an-array](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0912-sort-an-array) |
## Counting
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0347-top-k-frequent-elements) |
| [0387-first-unique-character-in-a-string](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0387-first-unique-character-in-a-string) |
| [1079-letter-tile-possibilities](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1079-letter-tile-possibilities) |
| [2133-number-of-pairs-of-strings-with-concatenation-equal-to-target](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2133-number-of-pairs-of-strings-with-concatenation-equal-to-target) |
| [3016-minimum-number-of-pushes-to-type-word-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3016-minimum-number-of-pushes-to-type-word-ii) |
| [3737-count-subarrays-with-majority-element-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3737-count-subarrays-with-majority-element-i) |
## Quickselect
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0347-top-k-frequent-elements) |
## Prefix Sum
|  |
| ------- |
| [0238-product-of-array-except-self](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0238-product-of-array-except-self) |
| [0304-range-sum-query-2d-immutable](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0304-range-sum-query-2d-immutable) |
| [1732-find-the-highest-altitude](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1732-find-the-highest-altitude) |
| [2574-left-and-right-sum-differences](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2574-left-and-right-sum-differences) |
| [3699-number-of-zigzag-arrays-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3699-number-of-zigzag-arrays-i) |
| [3737-count-subarrays-with-majority-element-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3737-count-subarrays-with-majority-element-i) |
| [3739-count-subarrays-with-majority-element-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3739-count-subarrays-with-majority-element-ii) |
## Union Find
|  |
| ------- |
| [0128-longest-consecutive-sequence](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0128-longest-consecutive-sequence) |
## Linked List
|  |
| ------- |
| [0002-add-two-numbers](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0002-add-two-numbers) |
| [0019-remove-nth-node-from-end-of-list](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0019-remove-nth-node-from-end-of-list) |
| [0021-merge-two-sorted-lists](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0021-merge-two-sorted-lists) |
| [0023-merge-k-sorted-lists](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0023-merge-k-sorted-lists) |
| [0092-reverse-linked-list-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0092-reverse-linked-list-ii) |
| [0138-copy-list-with-random-pointer](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0138-copy-list-with-random-pointer) |
| [0141-linked-list-cycle](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0141-linked-list-cycle) |
| [0143-reorder-list](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0143-reorder-list) |
| [0146-lru-cache](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0146-lru-cache) |
| [0206-reverse-linked-list](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0206-reverse-linked-list) |
| [0237-delete-node-in-a-linked-list](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0237-delete-node-in-a-linked-list) |
| [0460-lfu-cache](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0460-lfu-cache) |
| [0622-design-circular-queue](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0622-design-circular-queue) |
| [0705-design-hashset](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0705-design-hashset) |
| [0706-design-hashmap](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0706-design-hashmap) |
| [2095-delete-the-middle-node-of-a-linked-list](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2095-delete-the-middle-node-of-a-linked-list) |
| [2807-insert-greatest-common-divisors-in-linked-list](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2807-insert-greatest-common-divisors-in-linked-list) |
## Math
|  |
| ------- |
| [0002-add-two-numbers](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0002-add-two-numbers) |
| [0062-unique-paths](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0062-unique-paths) |
| [0070-climbing-stairs](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0070-climbing-stairs) |
| [0168-excel-sheet-column-title](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0168-excel-sheet-column-title) |
| [0628-maximum-product-of-three-numbers](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0628-maximum-product-of-three-numbers) |
| [0867-new-21-game](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0867-new-21-game) |
| [0877-stone-game](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0877-stone-game) |
| [1071-greatest-common-divisor-of-strings](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1071-greatest-common-divisor-of-strings) |
| [1199-minimum-time-to-build-blocks](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1199-minimum-time-to-build-blocks) |
| [1344-angle-between-hands-of-a-clock](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1344-angle-between-hands-of-a-clock) |
| [1406-stone-game-iii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1406-stone-game-iii) |
| [1448-maximum-69-number](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1448-maximum-69-number) |
| [1840-maximum-building-height](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1840-maximum-building-height) |
| [1863-sum-of-all-subset-xor-totals](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1863-sum-of-all-subset-xor-totals) |
| [1979-find-greatest-common-divisor-of-array](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1979-find-greatest-common-divisor-of-array) |
| [2450-minimum-replacements-to-sort-the-array](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2450-minimum-replacements-to-sort-the-array) |
| [2807-insert-greatest-common-divisors-in-linked-list](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2807-insert-greatest-common-divisors-in-linked-list) |
| [3014-minimum-number-of-pushes-to-type-word-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3014-minimum-number-of-pushes-to-type-word-i) |
| [3336-find-the-number-of-subsequences-with-equal-gcd](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3336-find-the-number-of-subsequences-with-equal-gcd) |
| [3348-smallest-divisible-digit-product-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3348-smallest-divisible-digit-product-ii) |
| [3513-number-of-unique-xor-triplets-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3513-number-of-unique-xor-triplets-i) |
| [3558-number-of-ways-to-assign-edge-weights-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3558-number-of-ways-to-assign-edge-weights-i) |
| [3559-number-of-ways-to-assign-edge-weights-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3559-number-of-ways-to-assign-edge-weights-ii) |
| [3700-number-of-zigzag-arrays-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3700-number-of-zigzag-arrays-ii) |
| [3753-total-waviness-of-numbers-in-range-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3753-total-waviness-of-numbers-in-range-ii) |
| [3754-concatenate-non-zero-digits-and-multiply-by-sum-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3754-concatenate-non-zero-digits-and-multiply-by-sum-i) |
## Recursion
|  |
| ------- |
| [0002-add-two-numbers](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0002-add-two-numbers) |
| [0021-merge-two-sorted-lists](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0021-merge-two-sorted-lists) |
| [0143-reorder-list](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0143-reorder-list) |
| [0206-reverse-linked-list](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0206-reverse-linked-list) |
## Sliding Window
|  |
| ------- |
| [0003-longest-substring-without-repeating-characters](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0003-longest-substring-without-repeating-characters) |
| [0219-contains-duplicate-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0219-contains-duplicate-ii) |
| [0867-new-21-game](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0867-new-21-game) |
| [1358-number-of-substrings-containing-all-three-characters](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1358-number-of-substrings-containing-all-three-characters) |
| [2958-length-of-longest-subarray-with-at-most-k-frequency](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2958-length-of-longest-subarray-with-at-most-k-frequency) |
## Dynamic Programming
|  |
| ------- |
| [0022-generate-parentheses](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0022-generate-parentheses) |
| [0042-trapping-rain-water](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0042-trapping-rain-water) |
| [0062-unique-paths](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0062-unique-paths) |
| [0070-climbing-stairs](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0070-climbing-stairs) |
| [0122-best-time-to-buy-and-sell-stock-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0122-best-time-to-buy-and-sell-stock-ii) |
| [0124-binary-tree-maximum-path-sum](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0124-binary-tree-maximum-path-sum) |
| [0131-palindrome-partitioning](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0131-palindrome-partitioning) |
| [0542-01-matrix](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0542-01-matrix) |
| [0741-cherry-pickup](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0741-cherry-pickup) |
| [0773-sliding-puzzle](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0773-sliding-puzzle) |
| [0867-new-21-game](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0867-new-21-game) |
| [0877-stone-game](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0877-stone-game) |
| [0934-bitwise-ors-of-subarrays](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0934-bitwise-ors-of-subarrays) |
| [1406-stone-game-iii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1406-stone-game-iii) |
| [3336-find-the-number-of-subsequences-with-equal-gcd](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3336-find-the-number-of-subsequences-with-equal-gcd) |
| [3534-path-existence-queries-in-a-graph-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3534-path-existence-queries-in-a-graph-ii) |
| [3559-number-of-ways-to-assign-edge-weights-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3559-number-of-ways-to-assign-edge-weights-ii) |
| [3620-network-recovery-pathways](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3620-network-recovery-pathways) |
| [3699-number-of-zigzag-arrays-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3699-number-of-zigzag-arrays-i) |
| [3700-number-of-zigzag-arrays-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3700-number-of-zigzag-arrays-ii) |
| [3753-total-waviness-of-numbers-in-range-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3753-total-waviness-of-numbers-in-range-ii) |
## Tree
|  |
| ------- |
| [0094-binary-tree-inorder-traversal](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0094-binary-tree-inorder-traversal) |
| [0124-binary-tree-maximum-path-sum](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0124-binary-tree-maximum-path-sum) |
| [0703-kth-largest-element-in-a-stream](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0703-kth-largest-element-in-a-stream) |
| [2196-create-binary-tree-from-descriptions](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2196-create-binary-tree-from-descriptions) |
| [3558-number-of-ways-to-assign-edge-weights-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3558-number-of-ways-to-assign-edge-weights-i) |
| [3559-number-of-ways-to-assign-edge-weights-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3559-number-of-ways-to-assign-edge-weights-ii) |
## Depth-First Search
|  |
| ------- |
| [0079-word-search](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0079-word-search) |
| [0094-binary-tree-inorder-traversal](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0094-binary-tree-inorder-traversal) |
| [0124-binary-tree-maximum-path-sum](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0124-binary-tree-maximum-path-sum) |
| [0130-surrounded-regions](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0130-surrounded-regions) |
| [0200-number-of-islands](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0200-number-of-islands) |
| [0207-course-schedule](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0207-course-schedule) |
| [0210-course-schedule-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0210-course-schedule-ii) |
| [0269-alien-dictionary](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0269-alien-dictionary) |
| [0323-number-of-connected-components-in-an-undirected-graph](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0323-number-of-connected-components-in-an-undirected-graph) |
| [0463-island-perimeter](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0463-island-perimeter) |
| [0547-number-of-provinces](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0547-number-of-provinces) |
| [0694-number-of-distinct-islands](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0694-number-of-distinct-islands) |
| [0733-flood-fill](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0733-flood-fill) |
| [0785-is-graph-bipartite](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0785-is-graph-bipartite) |
| [0802-find-eventual-safe-states](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0802-find-eventual-safe-states) |
| [1020-number-of-enclaves](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1020-number-of-enclaves) |
| [1631-path-with-minimum-effort](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1631-path-with-minimum-effort) |
| [1858-longest-word-with-all-prefixes](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1858-longest-word-with-all-prefixes) |
| [2685-count-the-number-of-complete-components](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2685-count-the-number-of-complete-components) |
| [3310-remove-methods-from-project](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3310-remove-methods-from-project) |
| [3558-number-of-ways-to-assign-edge-weights-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3558-number-of-ways-to-assign-edge-weights-i) |
| [3559-number-of-ways-to-assign-edge-weights-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3559-number-of-ways-to-assign-edge-weights-ii) |
## Binary Tree
|  |
| ------- |
| [0094-binary-tree-inorder-traversal](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0094-binary-tree-inorder-traversal) |
| [0124-binary-tree-maximum-path-sum](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0124-binary-tree-maximum-path-sum) |
| [0703-kth-largest-element-in-a-stream](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0703-kth-largest-element-in-a-stream) |
| [2196-create-binary-tree-from-descriptions](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2196-create-binary-tree-from-descriptions) |
## Two Pointers
|  |
| ------- |
| [0019-remove-nth-node-from-end-of-list](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0019-remove-nth-node-from-end-of-list) |
| [0042-trapping-rain-water](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0042-trapping-rain-water) |
| [0075-sort-colors](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0075-sort-colors) |
| [0141-linked-list-cycle](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0141-linked-list-cycle) |
| [0143-reorder-list](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0143-reorder-list) |
| [0287-find-the-duplicate-number](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0287-find-the-duplicate-number) |
| [0344-reverse-string](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0344-reverse-string) |
| [2095-delete-the-middle-node-of-a-linked-list](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2095-delete-the-middle-node-of-a-linked-list) |
| [3534-path-existence-queries-in-a-graph-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3534-path-existence-queries-in-a-graph-ii) |
## Stack
|  |
| ------- |
| [0042-trapping-rain-water](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0042-trapping-rain-water) |
| [0094-binary-tree-inorder-traversal](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0094-binary-tree-inorder-traversal) |
| [0143-reorder-list](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0143-reorder-list) |
| [0682-baseball-game](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0682-baseball-game) |
| [0739-daily-temperatures](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0739-daily-temperatures) |
| [1081-smallest-subsequence-of-distinct-characters](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1081-smallest-subsequence-of-distinct-characters) |
## Monotonic Stack
|  |
| ------- |
| [0042-trapping-rain-water](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0042-trapping-rain-water) |
| [0739-daily-temperatures](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0739-daily-temperatures) |
| [1081-smallest-subsequence-of-distinct-characters](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1081-smallest-subsequence-of-distinct-characters) |
## Bit Manipulation
|  |
| ------- |
| [0078-subsets](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0078-subsets) |
| [0090-subsets-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0090-subsets-ii) |
| [0136-single-number](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0136-single-number) |
| [0287-find-the-duplicate-number](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0287-find-the-duplicate-number) |
| [0934-bitwise-ors-of-subarrays](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0934-bitwise-ors-of-subarrays) |
| [1863-sum-of-all-subset-xor-totals](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1863-sum-of-all-subset-xor-totals) |
| [2503-longest-subarray-with-maximum-bitwise-and](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2503-longest-subarray-with-maximum-bitwise-and) |
| [3513-number-of-unique-xor-triplets-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3513-number-of-unique-xor-triplets-i) |
| [3534-path-existence-queries-in-a-graph-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3534-path-existence-queries-in-a-graph-ii) |
| [3559-number-of-ways-to-assign-edge-weights-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3559-number-of-ways-to-assign-edge-weights-ii) |
| [3702-longest-subsequence-with-non-zero-bitwise-xor](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3702-longest-subsequence-with-non-zero-bitwise-xor) |
## Brainteaser
|  |
| ------- |
| [2503-longest-subarray-with-maximum-bitwise-and](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2503-longest-subarray-with-maximum-bitwise-and) |
## Enumeration
|  |
| ------- |
| [1863-sum-of-all-subset-xor-totals](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1863-sum-of-all-subset-xor-totals) |
| [3020-find-the-maximum-number-of-elements-in-subset](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3020-find-the-maximum-number-of-elements-in-subset) |
| [3221-find-the-peaks](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3221-find-the-peaks) |
| [3499-maximize-active-section-with-trade-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3499-maximize-active-section-with-trade-i) |
## Trie
|  |
| ------- |
| [0014-longest-common-prefix](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0014-longest-common-prefix) |
| [1858-longest-word-with-all-prefixes](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1858-longest-word-with-all-prefixes) |
## Queue
|  |
| ------- |
| [0387-first-unique-character-in-a-string](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0387-first-unique-character-in-a-string) |
| [0622-design-circular-queue](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0622-design-circular-queue) |
## Greedy
|  |
| ------- |
| [0122-best-time-to-buy-and-sell-stock-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0122-best-time-to-buy-and-sell-stock-ii) |
| [0860-lemonade-change](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0860-lemonade-change) |
| [1081-smallest-subsequence-of-distinct-characters](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1081-smallest-subsequence-of-distinct-characters) |
| [1199-minimum-time-to-build-blocks](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1199-minimum-time-to-build-blocks) |
| [1448-maximum-69-number](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1448-maximum-69-number) |
| [1833-maximum-ice-cream-bars](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1833-maximum-ice-cream-bars) |
| [1846-maximum-element-after-decreasing-and-rearranging](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1846-maximum-element-after-decreasing-and-rearranging) |
| [2144-minimum-cost-of-buying-candies-with-discount](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2144-minimum-cost-of-buying-candies-with-discount) |
| [2450-minimum-replacements-to-sort-the-array](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2450-minimum-replacements-to-sort-the-array) |
| [3014-minimum-number-of-pushes-to-type-word-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3014-minimum-number-of-pushes-to-type-word-i) |
| [3016-minimum-number-of-pushes-to-type-word-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3016-minimum-number-of-pushes-to-type-word-ii) |
| [3348-smallest-divisible-digit-product-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3348-smallest-divisible-digit-product-ii) |
| [3534-path-existence-queries-in-a-graph-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3534-path-existence-queries-in-a-graph-ii) |
| [3689-maximum-total-subarray-value-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3689-maximum-total-subarray-value-i) |
## Binary Search
|  |
| ------- |
| [0081-search-in-rotated-sorted-array-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0081-search-in-rotated-sorted-array-ii) |
| [0287-find-the-duplicate-number](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0287-find-the-duplicate-number) |
| [0704-binary-search](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0704-binary-search) |
| [1631-path-with-minimum-effort](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1631-path-with-minimum-effort) |
| [2812-find-the-safest-path-in-a-grid](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2812-find-the-safest-path-in-a-grid) |
| [3532-path-existence-queries-in-a-graph-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3532-path-existence-queries-in-a-graph-i) |
| [3534-path-existence-queries-in-a-graph-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3534-path-existence-queries-in-a-graph-ii) |
| [3620-network-recovery-pathways](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3620-network-recovery-pathways) |
## Probability and Statistics
|  |
| ------- |
| [0867-new-21-game](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0867-new-21-game) |
## Design
|  |
| ------- |
| [0146-lru-cache](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0146-lru-cache) |
| [0304-range-sum-query-2d-immutable](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0304-range-sum-query-2d-immutable) |
| [0460-lfu-cache](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0460-lfu-cache) |
| [0622-design-circular-queue](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0622-design-circular-queue) |
| [0703-kth-largest-element-in-a-stream](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0703-kth-largest-element-in-a-stream) |
| [0705-design-hashset](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0705-design-hashset) |
| [0706-design-hashmap](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0706-design-hashmap) |
## Hash Function
|  |
| ------- |
| [0694-number-of-distinct-islands](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0694-number-of-distinct-islands) |
| [0705-design-hashset](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0705-design-hashset) |
| [0706-design-hashmap](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0706-design-hashmap) |
## Merge Sort
|  |
| ------- |
| [0023-merge-k-sorted-lists](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0023-merge-k-sorted-lists) |
| [0912-sort-an-array](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0912-sort-an-array) |
| [3737-count-subarrays-with-majority-element-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3737-count-subarrays-with-majority-element-i) |
| [3739-count-subarrays-with-majority-element-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3739-count-subarrays-with-majority-element-ii) |
## Radix Sort
|  |
| ------- |
| [0912-sort-an-array](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0912-sort-an-array) |
## Counting Sort
|  |
| ------- |
| [0912-sort-an-array](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0912-sort-an-array) |
| [1833-maximum-ice-cream-bars](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1833-maximum-ice-cream-bars) |
## Backtracking
|  |
| ------- |
| [0017-letter-combinations-of-a-phone-number](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0017-letter-combinations-of-a-phone-number) |
| [0022-generate-parentheses](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0022-generate-parentheses) |
| [0039-combination-sum](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0039-combination-sum) |
| [0040-combination-sum-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0040-combination-sum-ii) |
| [0046-permutations](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0046-permutations) |
| [0047-permutations-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0047-permutations-ii) |
| [0077-combinations](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0077-combinations) |
| [0078-subsets](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0078-subsets) |
| [0079-word-search](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0079-word-search) |
| [0090-subsets-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0090-subsets-ii) |
| [0093-restore-ip-addresses](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0093-restore-ip-addresses) |
| [0126-word-ladder-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0126-word-ladder-ii) |
| [0131-palindrome-partitioning](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0131-palindrome-partitioning) |
| [0291-word-pattern-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0291-word-pattern-ii) |
| [0773-sliding-puzzle](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0773-sliding-puzzle) |
| [1079-letter-tile-possibilities](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1079-letter-tile-possibilities) |
| [1863-sum-of-all-subset-xor-totals](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1863-sum-of-all-subset-xor-totals) |
| [3348-smallest-divisible-digit-product-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3348-smallest-divisible-digit-product-ii) |
## Breadth-First Search
|  |
| ------- |
| [0126-word-ladder-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0126-word-ladder-ii) |
| [0127-word-ladder](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0127-word-ladder) |
| [0130-surrounded-regions](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0130-surrounded-regions) |
| [0200-number-of-islands](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0200-number-of-islands) |
| [0207-course-schedule](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0207-course-schedule) |
| [0210-course-schedule-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0210-course-schedule-ii) |
| [0269-alien-dictionary](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0269-alien-dictionary) |
| [0323-number-of-connected-components-in-an-undirected-graph](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0323-number-of-connected-components-in-an-undirected-graph) |
| [0463-island-perimeter](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0463-island-perimeter) |
| [0542-01-matrix](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0542-01-matrix) |
| [0547-number-of-provinces](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0547-number-of-provinces) |
| [0694-number-of-distinct-islands](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0694-number-of-distinct-islands) |
| [0733-flood-fill](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0733-flood-fill) |
| [0773-sliding-puzzle](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0773-sliding-puzzle) |
| [0785-is-graph-bipartite](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0785-is-graph-bipartite) |
| [0802-find-eventual-safe-states](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0802-find-eventual-safe-states) |
| [0994-rotting-oranges](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0994-rotting-oranges) |
| [1020-number-of-enclaves](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1020-number-of-enclaves) |
| [1631-path-with-minimum-effort](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1631-path-with-minimum-effort) |
| [2685-count-the-number-of-complete-components](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2685-count-the-number-of-complete-components) |
| [2812-find-the-safest-path-in-a-grid](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2812-find-the-safest-path-in-a-grid) |
| [3310-remove-methods-from-project](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3310-remove-methods-from-project) |
## Memoization
|  |
| ------- |
| [0070-climbing-stairs](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0070-climbing-stairs) |
| [0773-sliding-puzzle](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0773-sliding-puzzle) |
## Doubly-Linked List
|  |
| ------- |
| [0146-lru-cache](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0146-lru-cache) |
| [0460-lfu-cache](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0460-lfu-cache) |
## Simulation
|  |
| ------- |
| [0682-baseball-game](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0682-baseball-game) |
| [1929-concatenation-of-array](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1929-concatenation-of-array) |
| [3614-process-string-with-special-operations-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3614-process-string-with-special-operations-ii) |
## Segment Tree
|  |
| ------- |
| [3737-count-subarrays-with-majority-element-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3737-count-subarrays-with-majority-element-i) |
| [3739-count-subarrays-with-majority-element-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3739-count-subarrays-with-majority-element-ii) |
## Union-Find
|  |
| ------- |
| [0130-surrounded-regions](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0130-surrounded-regions) |
| [0200-number-of-islands](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0200-number-of-islands) |
| [0323-number-of-connected-components-in-an-undirected-graph](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0323-number-of-connected-components-in-an-undirected-graph) |
| [0547-number-of-provinces](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0547-number-of-provinces) |
| [0694-number-of-distinct-islands](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0694-number-of-distinct-islands) |
| [0785-is-graph-bipartite](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0785-is-graph-bipartite) |
| [1020-number-of-enclaves](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1020-number-of-enclaves) |
| [1631-path-with-minimum-effort](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1631-path-with-minimum-effort) |
| [2685-count-the-number-of-complete-components](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2685-count-the-number-of-complete-components) |
| [2812-find-the-safest-path-in-a-grid](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2812-find-the-safest-path-in-a-grid) |
| [3532-path-existence-queries-in-a-graph-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3532-path-existence-queries-in-a-graph-i) |
## Graph Theory
|  |
| ------- |
| [0207-course-schedule](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0207-course-schedule) |
| [0210-course-schedule-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0210-course-schedule-ii) |
| [0269-alien-dictionary](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0269-alien-dictionary) |
| [0323-number-of-connected-components-in-an-undirected-graph](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0323-number-of-connected-components-in-an-undirected-graph) |
| [0547-number-of-provinces](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0547-number-of-provinces) |
| [0785-is-graph-bipartite](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0785-is-graph-bipartite) |
| [0802-find-eventual-safe-states](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0802-find-eventual-safe-states) |
| [2685-count-the-number-of-complete-components](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2685-count-the-number-of-complete-components) |
| [3310-remove-methods-from-project](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3310-remove-methods-from-project) |
| [3532-path-existence-queries-in-a-graph-i](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3532-path-existence-queries-in-a-graph-i) |
| [3534-path-existence-queries-in-a-graph-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3534-path-existence-queries-in-a-graph-ii) |
| [3620-network-recovery-pathways](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3620-network-recovery-pathways) |
## Topological Sort
|  |
| ------- |
| [0207-course-schedule](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0207-course-schedule) |
| [0210-course-schedule-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0210-course-schedule-ii) |
| [0269-alien-dictionary](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0269-alien-dictionary) |
| [0802-find-eventual-safe-states](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0802-find-eventual-safe-states) |
| [3620-network-recovery-pathways](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3620-network-recovery-pathways) |
## Shortest Path
|  |
| ------- |
| [3620-network-recovery-pathways](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3620-network-recovery-pathways) |
## Binary Search Tree
|  |
| ------- |
| [0703-kth-largest-element-in-a-stream](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0703-kth-largest-element-in-a-stream) |
## Data Stream
|  |
| ------- |
| [0703-kth-largest-element-in-a-stream](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0703-kth-largest-element-in-a-stream) |
## Combinatorics
|  |
| ------- |
| [0062-unique-paths](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0062-unique-paths) |
| [1863-sum-of-all-subset-xor-totals](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1863-sum-of-all-subset-xor-totals) |
## Number Theory
|  |
| ------- |
| [1979-find-greatest-common-divisor-of-array](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1979-find-greatest-common-divisor-of-array) |
| [2807-insert-greatest-common-divisors-in-linked-list](https://github.com/RaghhavMalani/leetcode-progress/tree/master/2807-insert-greatest-common-divisors-in-linked-list) |
| [3336-find-the-number-of-subsequences-with-equal-gcd](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3336-find-the-number-of-subsequences-with-equal-gcd) |
| [3348-smallest-divisible-digit-product-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/3348-smallest-divisible-digit-product-ii) |
## Game Theory
|  |
| ------- |
| [0877-stone-game](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0877-stone-game) |
| [1406-stone-game-iii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/1406-stone-game-iii) |
## Directed Acyclic Graph
|  |
| ------- |
| [0207-course-schedule](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0207-course-schedule) |
| [0269-alien-dictionary](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0269-alien-dictionary) |
## Graph Coloring
|  |
| ------- |
| [0785-is-graph-bipartite](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0785-is-graph-bipartite) |
## Bipartite Graph
|  |
| ------- |
| [0785-is-graph-bipartite](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0785-is-graph-bipartite) |
## Bidirectional Search
|  |
| ------- |
| [0126-word-ladder-ii](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0126-word-ladder-ii) |
| [0127-word-ladder](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0127-word-ladder) |
## Kosaraju's Algorithm
|  |
| ------- |
| [0802-find-eventual-safe-states](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0802-find-eventual-safe-states) |
## Tarjan's SCC Algorithm
|  |
| ------- |
| [0802-find-eventual-safe-states](https://github.com/RaghhavMalani/leetcode-progress/tree/master/0802-find-eventual-safe-states) |
<!---LeetCode Topics End-->