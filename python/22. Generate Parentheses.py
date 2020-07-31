class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        self.dfs(n,0,0,'',res)
        return res

    def dfs(self, n, left, right,temp, res):
        print(left,right)
        if len(temp)==n*2:
            res.append(temp)
            return
        if left<n:
            self.dfs(n,left+1,right,temp+'(',res)
        if right<left:
            self.dfs(n,left,right+1,temp+')',res)
if __name__ == '__main__':
    a=Solution()
    print(a.generateParenthesis(3))