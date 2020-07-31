class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        l=[]
        for i in s:
            if i.isalnum():
                l.append(i)
        s=''.join(l).upper()

        if s==s[::-1]:
            return True
        return False

if __name__ == '__main__':
    a=Solution()
    print(a.isPalindrome("A man, a plan, a canal: Panama"))