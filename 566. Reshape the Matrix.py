class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        if len(nums)*len(nums[0])!=r*c:
            return nums
        else:
            newLis=[[0 for col in range(c)] for row in range(r)]
            row=0
            col=0
            for i in range(len(nums)):
                for j in range(len(nums[0])):
                    newLis[row][col]=nums[i][j]
                    if col==c-1:
                        row+=1
                        col=0

                    else:
                        col+=1
            return newLis
if __name__ == '__main__':
    a=Solution()
    print(a.matrixReshape([[1,2],
 [3,4]],1,4))