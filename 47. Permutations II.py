class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(nums,[],res,[])
        return res

    def dfs(self, nums, temp, res,walked):
        print(temp)
        if len(temp) ==len(nums):
            if temp not in res:
                res.append(temp)
            return
        for i in range(len(nums)):
            if i not in walked:
                self.dfs(nums,temp+[nums[i]],res,walked+[i])

if __name__ == '__main__':
    a=Solution()
    print(a.permuteUnique([1,1,2]))