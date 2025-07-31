class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i, char in enumerate(strs[0]):
            for other_str in strs[1:]:
                if i >= len(other_str) or other_str[i] != char:
                    return strs[0][:i]
        
        return strs[0]