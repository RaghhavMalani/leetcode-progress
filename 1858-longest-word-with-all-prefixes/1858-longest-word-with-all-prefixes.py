class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda word: (len(word), word))

        valid = set()
        answer = ""

        for word in words:
            if len(word) == 1 or word[:-1] in valid:
                valid.add(word)

                if len(word) > len(answer):
                    answer = word

        return answer