class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)

if __name__ == '__main__':
    a=Solution()
    print(a.strStr('hello','l'))