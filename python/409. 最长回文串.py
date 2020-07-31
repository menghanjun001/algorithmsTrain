class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap={}
        ou=0
        jiList=[]
        for i in s:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        for i in hashmap:
            if hashmap[i]%2==0:
                ou+=hashmap[i]
            else:
                jiList.append(hashmap[i])
                if hashmap[i]>0:
                    ou+=hashmap[i]-1
        if not jiList:
            return ou
        else:
            return ou+1
