class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp_max = [nums[0]] * len(nums)
        dp_min = [nums[0]] * len(nums)
        for i in range(1,len(nums)):
            # print(dp_max[i-1]*nums[i],dp_min[i-1]*nums[i],nums[i])
            dp_max[i]=max(dp_max[i-1]*nums[i],dp_min[i-1]*nums[i],nums[i])
            dp_min[i]=min(dp_max[i-1]*nums[i],dp_min[i-1]*nums[i],nums[i])
            # print(dp_max[i],dp_min[i])
        return max(dp_max)

if __name__ == '__main__':
    a=Solution()
    print(a.maxProduct([2,3,-2,4]))
