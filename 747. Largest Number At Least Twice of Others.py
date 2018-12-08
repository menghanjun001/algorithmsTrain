class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        inde=nums.index(max(nums))
        maxNum=nums.pop(inde)
        if maxNum>=2*max(nums):
            return inde
        else:
            return -1