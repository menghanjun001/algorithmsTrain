class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        price_low=prices[0]
        profit=0
        for i in prices:
            price_low=min(price_low,i)
            profit=max(profit,i-price_low)

        return profit

if __name__ == '__main__':
    a=Solution()
    print(a.maxProfit([2,4,1]))