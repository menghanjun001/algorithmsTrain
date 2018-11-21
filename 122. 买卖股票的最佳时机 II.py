class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        for i in range(1,len(prices)):
            if prices[i]-prices[i-1]>0:
                profit+=prices[i]-prices[i-1]
        return profit

# if __name__ == '__main__':
#     a=Solution()
#     print(a.maxProfit([9,1,2,3,4,5,6]))