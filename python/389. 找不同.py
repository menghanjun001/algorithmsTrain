class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res=0
        for ch in s+t:
            res^=ord(ch)
        return chr(res)

