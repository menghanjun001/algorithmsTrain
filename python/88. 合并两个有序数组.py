class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m,len(nums1)):
            if nums1[i]==0:
                nums1[i]=nums2.pop()
        nums1[:]=self.quickSort(nums1)
        # return nums1

    def quickSort(self,lis):
        if not lis:
            return []
        pivot=lis[0]
        left=self.quickSort([i for i in lis[1:] if i<pivot])
        right=self.quickSort([i for i in lis[1:] if i>=pivot])
        return left+[pivot]+right
if __name__ == '__main__':
    a=Solution()
    print(a.merge([1,2,3,0,0,0],3,[2,5,6],3))