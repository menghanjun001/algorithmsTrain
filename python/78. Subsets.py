class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(nums,0,[],res)
        return res

    def dfs(self, nums, start, temp, res):
        res.append(temp)
        if start==len(nums):
            return
        for i in range(start,len(nums)):
            self.dfs(nums,i+1,temp+[nums[i]],res)

if __name__ == '__main__':
    a=Solution()
    print(a.subsets([1,2,3]))