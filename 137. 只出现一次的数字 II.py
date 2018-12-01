class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap={}
        for i in nums:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        for i in hashmap:
            if hashmap[i]==1:
                return i