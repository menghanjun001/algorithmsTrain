class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        inc=True
        dec=True
        for i in range(1,len(A)):
            # print(A[i-1],A[i])
            if A[i]<A[i-1]:
                inc=False
            if A[i]>A[i-1]:
                dec=False
            # print(inc,dec)
        return inc or dec
if __name__ == '__main__':
    a=Solution()
    print(a.isMonotonic([1,3,2]))