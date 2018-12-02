class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashmp={}
        for i in range(len(nums)):
            if nums[i] not in hashmp:
                hashmp[nums[i]]=i
            else:
                print(i)
                print(hashmp[nums[i]])
                if abs(i-hashmp[nums[i]])<=k:
                    return True
                hashmp[nums[i]]=i
        return False
if __name__ == '__main__':
    a=Solution()
    print(a.containsNearbyDuplicate([1,0,1,1],1))
