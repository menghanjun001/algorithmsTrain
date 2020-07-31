class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        words=s.strip(' ').split(' ')
        return len(words[-1])

if __name__ == '__main__':
    a=Solution()
    print(a.lengthOfLastWord('a '))