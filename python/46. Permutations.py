class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(nums,[],res)
        return res

    def dfs(self, nums, temp, res):
        if len(temp)==len(nums):
            res.append(temp)
            return 
        for i in range(len(nums)):
            if nums[i] in temp:
                continue
            self.dfs(nums,temp+[nums[i]],res)
            
if __name__ == '__main__':
    a=Solution()
    print(a.permute([1,2,3]))
        
    