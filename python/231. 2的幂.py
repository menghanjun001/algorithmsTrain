class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<0:
            return False
        else:
            if bin(n).count('1')==1:
                return True
            return False