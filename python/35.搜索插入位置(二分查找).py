class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low=0
        high=len(nums)
        while low<high:
            # print('low  '+str(low))
            # print('high '+str(high))
            mid=(high+low)//2
            if target<nums[mid]:
                high=mid
            elif target>nums[mid]:
                low=mid+1
            else:
                return mid
        return low

if __name__ == '__main__':
    a=Solution()
    print(a.searchInsert([1,3,5,6],2))