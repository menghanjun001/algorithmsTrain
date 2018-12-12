class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        add=lambda x,y,z:x*y*z
        return max(add(nums[-1],nums[-2],nums[-3]),
                   add(nums[-1],nums[0],nums[1]))