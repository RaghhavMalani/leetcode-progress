class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbr_map = {}

        for word in dictionary:
            abbr = self.get_abbr(word)

            if abbr not in self.abbr_map:
                self.abbr_map[abbr] = word
            else:
                if self.abbr_map[abbr] != word:
                    self.abbr_map[abbr] = ""

    def get_abbr(self, word: str) -> str:
        n = len(word)
        if n <= 2:
            return word

        return word[0] + str(n - 2) + word[-1]

    def isUnique(self, word: str) -> bool:
        abbr = self.get_abbr(word)

        if abbr not in self.abbr_map:
            return True
        return self.abbr_map[abbr] == word


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)