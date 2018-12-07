class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rowList=[]
        colList=[]
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col]==0:
                    if row not in rowList:
                        rowList.append(row)
                    if col not in colList:
                        colList.append(col)
        for row in rowList:
            matrix[row]=[0]*len(matrix[0])
        for col in colList:
            for row in range(len(matrix)):
                matrix[row][col]=0