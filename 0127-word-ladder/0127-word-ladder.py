class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])

        if beginWord in words:
            words.remove(beginWord)

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for index in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == word[index]:
                        continue

                    new_word = word[:index] + ch + word[index + 1:]

                    if new_word in words:
                        words.remove(new_word)
                        queue.append((new_word, steps + 1))

        return 0