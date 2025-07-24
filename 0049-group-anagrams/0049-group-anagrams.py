class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = defaultdict(list)

        for i in range(len(strs)):
            count = [0] * 26
            for char in strs[i]:
                count[ord(char) - ord("a")] += 1

            map[tuple(count)].append(strs[i])

        return map.values()
        
            
