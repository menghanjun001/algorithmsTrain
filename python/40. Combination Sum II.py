class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]

        self.dfs(candidates,target,0,[],res)
        return res

    def dfs(self, candidates, target, start, temp, res):
        # print(temp)
        if sum(temp) >target:
            return
        if sum(temp)==target and sorted(temp) not in res:
            res.append(sorted(temp))
            return
        for i in range(start,len(candidates)):
            self.dfs(candidates,target,i+1,temp+[candidates[i]],res)

if __name__ == '__main__':
    a=Solution()
    print(a.combinationSum2([10,1,2,7,6,1,5],8))