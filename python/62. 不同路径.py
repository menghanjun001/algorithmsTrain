# class Solution: #递归太耗时
#     def uniquePaths(self, m, n):
#         """
#         :type m: int
#         :type n: int
#         :rtype: int
#         """
#         if n==1 or m==1:
#             return 1
#         return self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)
import pprint


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        lis=[[0 for i in range(m)]for i in range(n)]
        for i in range(n):
            lis[i][0]=1
        for j in range(m):
            lis[0][j]=1
        for i in range(1,n):
            for j in range(1,m):
                lis[i][j]=lis[i-1][j]+lis[i][j-1]
        return lis[n-1][m-1]

if __name__ == '__main__':
    a=Solution()
    print(a.uniquePaths(7,3))