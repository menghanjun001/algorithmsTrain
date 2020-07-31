class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        dp=A
        for row in range(len(A)):
            for col in range(len(A[row])):
                if row!=0 and col!=0 and col!=len(A[row])-1:
                    dp[row][col]=min(dp[row-1][col-1],dp[row-1][col],dp[row-1][col+1])+A[row][col]
                elif row!=0 and col==0:
                    dp[row][col]=min(dp[row-1][col],dp[row-1][col+1])+A[row][col]
                elif row!=0 and col==len(A[row])-1:
                    dp[row][col]=min(dp[row-1][col-1],dp[row-1][col])+A[row][col]
        return min(dp[-1])
