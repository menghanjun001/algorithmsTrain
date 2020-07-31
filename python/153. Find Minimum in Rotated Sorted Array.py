class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        left=0
        right=len(nums)-1
        if nums[left]<nums[right]:
            return nums[0]
        while left+1 !=right:
            mid = (left + right) // 2
            if nums[mid]<nums[left] and nums[mid]<nums[right]:
                right=mid
            elif nums[mid]>nums[left] and nums[mid]>nums[right]:
                left=mid
        return nums[right]
if __name__ == '__main__':
    a=Solution()
    print(a.findMin([1,2,3]))