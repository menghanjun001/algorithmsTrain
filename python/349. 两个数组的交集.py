class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        lis=[]
        for i in set(nums1):
            if i in set(nums2):
                lis.append(i)
        return lis