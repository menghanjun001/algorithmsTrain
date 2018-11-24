class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp=nums[0]
        maximum=nums[0]
        for i in range(1,len(nums)):
            if tmp<=0:
                tmp=nums[i]
            else:
                tmp+=nums[i]
            if maximum<tmp:
                maximum=tmp
        return maximum
if __name__ == '__main__':
    a=Solution()
    print(a.maxSubArray([1,2,3,-1,9]))