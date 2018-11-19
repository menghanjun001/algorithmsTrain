class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)):
        #     # print(nums[i])
        #     if nums[i]==0:
        #
        #         #nums.pop(i) 错误的
        #         nums.remove(nums[i])
        #         nums.append(0)
        news=[i for i in nums if i!=0]
        nums[:]=news+[0]*(len(nums)-len(news))
        #nums=news+[0]*(len(nums)-len(news))  是错的


if __name__ == '__main__':
    a=Solution()
    print(a.moveZeroes([0,1,0,3,12]))
