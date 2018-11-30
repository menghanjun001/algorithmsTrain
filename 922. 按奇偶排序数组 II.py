class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        lis=[0 for i in range(len(A))]
        ji=1
        ou=0
        for i in A:
            if i&1:
                lis[ji]=i
                ji+=2
            else:
                lis[ou]=i
                ou+=2
        return lis