class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=bin(n).replace('0b','')
        for i in range(1,len(s)):
            if s[i-1:i+1]=='00' or s[i-1:i+1]=='11':
                return False
        return True