# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        dp=[0,1,2]
        if number>=3:
            for i in range(3,number+1):
                dp.append(dp[i-1]+dp[i-2])
        return dp[number]