class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)<3:
            return max(nums)
        dp=nums
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        return max(dp)
if __name__ == '__main__':
    a=Solution()
    print(a.rob([2,7,9,3,1]))
