class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*(n+1)
        dp[0]=dp[1]=1
        #0个 1个节点情况只有一种
        for i in range(2,n+1):
            for j in range(i):          #总节点,j为左子树节点数目
                print(i,j,i-j-1)
                dp[i]+=dp[j]*dp[i-j-1] #输入2，有2 0 和1 1、、、 即把根节点算入一条子树中
                print(dp[i])
        return dp[n]

if __name__ == '__main__':
    a=Solution()
    print(a.numTrees(3))