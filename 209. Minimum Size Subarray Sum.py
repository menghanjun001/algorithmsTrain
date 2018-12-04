class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=0
        sumAll=0
        nums_len=len(nums)
        minLength = nums_len + 1
        while l<nums_len:

            if r<nums_len and sumAll <s:
                sumAll+=nums[r]
                r+=1
            else:
                sumAll-=nums[l]
                l+=1
            if sumAll>=s:
                minLength = min(minLength, r - l )  #r加的超过数组长度了草
        if minLength==nums_len+1:
            return 0
        return minLength
if __name__ == '__main__':
    a=Solution()
    print(a.minSubArrayLen(2,[1,1]))