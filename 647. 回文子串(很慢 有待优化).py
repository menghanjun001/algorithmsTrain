class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        #x+1是字符串长度
        for x in range(len(s)):
            for i in range(len(s) - x):
                if self.huiwen(s[i:i + x + 1]):
                    count+=1
        return count

    def huiwen(self, i):
        if i==i[::-1]:
            return True
        else:
            return False