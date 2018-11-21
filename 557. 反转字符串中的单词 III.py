class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss=[]
        for i in s.split(' '):
            ss.append(i[::-1])
        return ' '.join(ss)