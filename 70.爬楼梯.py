class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        li=[0,1,2]
        for i in range(3,n+1):
            li.append(li[i-1]+li[i-2])
        return li[n]
# if __name__ == '__main__':
#     a=Solution()
#     print(a.climbStairs(1))