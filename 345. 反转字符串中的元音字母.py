class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        left=0
        right=len(s)-1
        yuan='aeiouAEIOU'
        lis=list(s)
        while left<right:
            if lis[left] not in yuan:
                left+=1
            elif lis[right] not in yuan:
                right-=1
            else:
                lis[left],lis[right]=lis[right],lis[left]
                left+=1
                right-=1
        return ''.join(lis)