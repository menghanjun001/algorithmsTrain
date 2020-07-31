# from time import sleep
#
#
# class Solution(object):
#     def subsetsWithDup(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         res=[]
#         self.dfs(nums,[],[],res)
#         return res
#
#     def dfs(self, nums, temp, walked, res):
#         # sleep(1)
#         print(temp)
#         if sorted(temp) not in res:
#             res.append(sorted(temp))
#         for i in range(len(nums)):
#             if i not in walked:
#                 self.dfs(nums,temp+[nums[i]],walked+[i],res)
#         return
# if __name__ == '__main__':
#     a=Solution()
#     print(a.subsetsWithDup([1,2,3,4,5,6,7,8,10,0]))
from itertools import combinations, combinations_with_replacement


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        for i in range(len(nums)+1):
            res.extend(list(map(list,combinations(nums,i))))
        return res
if __name__ == '__main__':
    a=Solution()
    print(a.subsetsWithDup([1,2,2]))