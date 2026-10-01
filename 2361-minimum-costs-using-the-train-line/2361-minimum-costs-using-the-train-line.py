class Solution:
    def minimumCosts(self, regular: list[int], express: list[int], expressCost: int) -> list[int]:
        n = len(regular)

        reg = 0
        exp = expressCost
        ans = []

        for i in range(n):
            new_reg = min( reg + regular[i],exp + regular[i])

            new_exp = min(exp + express[i],reg + expressCost + express[i])

            reg = new_reg
            exp = new_exp

            ans.append(min(reg, exp))

        return ans