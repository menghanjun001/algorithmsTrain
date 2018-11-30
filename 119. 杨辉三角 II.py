class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res=[]
        ans=[]
        for i in range(rowIndex+1):
            res=[1]*(i+1)
            ans.append(res)
            for j in range(1,i):
                ans[i][j]=ans[i-1][j-1]+ans[i-1][j]
        return ans[rowIndex]
            