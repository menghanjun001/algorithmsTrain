class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        hashmap=[i for i in range(1,max(max(nums)+1,len(nums)+1))]
        return list(set(hashmap)-set(nums))
if __name__ == '__main__':
    a=Solution()
    print(a.findDisappearedNumbers([1,2,3,5,6,7]))