class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dp1=[1]
        dp2=[1]
        for i in range(len(nums)):
            dp1.append(nums[i]*dp1[i])
            dp2.append(nums[-1-i]*dp2[i])
        dp1.pop(0)
        dp2.pop(0)
        dp2.reverse()
        # print(dp1)
        # print(dp2)
        lis=[]
        for i in range(len(nums)):
            if i==0:
                lis.append(dp2[i+1])
            elif i==len(nums)-1:
                lis.append(dp1[i-1])
            else:
                lis.append(dp1[i-1]*dp2[i+1])
        return lis
if __name__ == '__main__':
    a=Solution()
    print(a.productExceptSelf([1,2,3,4]))