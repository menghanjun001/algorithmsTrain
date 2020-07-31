import random

#优化了快排后可以通过
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums=self.quickSort(nums)
        return nums[-k]
    def quickSort(self,lis):
        if not lis:
            return []
        index=random.randint(0,len(lis)-1)
        pivot=lis[index]
        left=self.quickSort([i for i in lis[0:index]+lis[index+1:len(lis)] if i<pivot])
        right=self.quickSort([i for i in lis[0:index]+lis[index+1:len(lis)] if i>=pivot])
        return left+[pivot]+right

if __name__ == '__main__':
    a=Solution()
    print(a.findKthLargest([2,1],2))