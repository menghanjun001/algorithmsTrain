class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in set(nums):
            if nums.count(i)>len(nums)//3:
                res.append(i)
        return res