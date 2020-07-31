class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
        for j in hashmap:
            if hashmap[j] > 1:
                return True
        return False


if __name__ == '__main__':
    a = Solution()
    print(a.containsDuplicate([1, 2, 3, 4]))
