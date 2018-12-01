class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashmap={}
        res=[]
        for i in nums:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        for j in hashmap:
            if hashmap[j]==1:
                res.append(j)
        return res