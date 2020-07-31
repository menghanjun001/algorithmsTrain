class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(candidates,target,0,[],res)
        return res
    def dfs(self,candidates,target,start,temp,res):
        if sum(temp)>target:
            return
        if sum(temp)==target:
            res.append(temp)
            return
        for i in range(start,len(candidates)):
            self.dfs(candidates,target,i,temp+[candidates[i]],res)
if __name__ == '__main__':
    a=Solution()
    print(a.combinationSum([2,3,5],8))