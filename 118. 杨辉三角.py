class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans=[]
        for i in range(numRows):
           lis=[1]*(i+1)
           ans.append(lis)
           for j in range(1,i):
               ans[i][j]=ans[i-1][j-1]+ans[i-1][j]
        return ans
if __name__ == '__main__':
    a=Solution()
    print(a.generate(5))
