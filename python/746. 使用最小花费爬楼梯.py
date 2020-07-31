class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp=list(range(len(cost)))
        dp[0]=dp[1]=0
        for i in range(2,len(cost)):
            dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        # print(dp)
        return min(dp[-1]+cost[-1],dp[-2]+cost[-2])

if __name__ == '__main__':
    a=Solution()
    print(a.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
# print(list(range(len([9,9,9]))))

