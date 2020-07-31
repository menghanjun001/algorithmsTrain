class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap={}
        for i in nums:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        for j in hashmap:
            if hashmap[j]>len(nums)/2:
                return j

# if __name__ == '__main__':
#     a=Solution()
#     print(a.majorityElement([3,2,3]))