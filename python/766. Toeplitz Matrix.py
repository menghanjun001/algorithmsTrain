class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for row in range(len(matrix)-1):
            for col in range(len(matrix[row])-1):
                if matrix[row][col]!=matrix[row+1][col+1]:
                    return False
        return True
