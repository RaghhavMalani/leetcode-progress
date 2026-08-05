class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words = set(wordList)
        
        if endWord not in words:
            return []

        parents = defaultdict(list)

        distance = {beginWord: 0}
        queue = deque([beginWord])

        while queue:
            word = queue.popleft()

            if word == endWord:
                continue

            for index in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == word[index]:
                        continue

                    new_word = (
                        word[:index]
                        + ch
                        + word[index + 1:]
                    )

                    if new_word not in words:
                        continue

                    if new_word not in distance:
                        distance[new_word] = distance[word] + 1
                        parents[new_word].append(word)
                        queue.append(new_word)

                    elif distance[new_word] == distance[word] + 1:
                        parents[new_word].append(word)

        if endWord not in distance:
            return []

        answer = []
        path = [endWord]

        def dfs(word):
            if word == beginWord:
                answer.append(path[::-1])
                return

            for parent in parents[word]:
                path.append(parent)
                dfs(parent)
                path.pop()

        dfs(endWord)

        return answer