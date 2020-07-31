class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i = len(matrix) - 1
        j = 0
        if i < 0:
            return False
        if not matrix[0]:
            return False
        mid = matrix[i][j]
        while (True):

            if mid < target:
                j += 1
            elif mid > target:
                i -= 1
            else:
                return True
            if i < 0 or j > len(matrix[0]) - 1:
                return False
            mid = matrix[i][j]