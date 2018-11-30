class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = ''.join(map(lambda x: str(x), nums))
        nums = s.split('0')
        # length=[]
        # for i in nums:
        #     length.append(len(i))
        return max(map(lambda x:len(x),nums))