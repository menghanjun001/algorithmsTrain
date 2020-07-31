class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(k,n,[1,2,3,4,5,6,7,8,9],1,[],res)
        return res

    def dfs(self, k, n,nums, start, temp, res):
        if k==0 and sum(temp)==n:
            res.append(temp)
            return
        for i in range(start,len(nums)+1):
            self.dfs(k-1,n,nums,i+1,temp+[i],res)
if __name__ == '__main__':
    a=Solution()
    print(a.combinationSum3(3,9))
