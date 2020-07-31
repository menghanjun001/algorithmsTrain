class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in findNums:
            for j in nums[nums.index(i):]:
                print(i,j)
                if j > i:
                    # print(i, j)
                    res.append(j)
                    break
                if j==nums[-1]:
                    res.append(-1)
        return res

if __name__ == '__main__':
    a=Solution()
    print(a.nextGreaterElement([4,1,2],
[1,3,4,2]
))