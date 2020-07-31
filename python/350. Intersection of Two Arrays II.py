class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d={}
        res=[]
        for i in nums1:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in nums2:
            if i in d and d[i]>0:
                d[i]-=1
                res.append(i)
        return res