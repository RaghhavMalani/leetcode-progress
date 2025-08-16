class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        
        num = str(num)

        new = num.replace('6','9',1)

        return int(new)