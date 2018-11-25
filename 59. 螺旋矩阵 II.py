import pprint


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix=[[0 for i in range(n)] for i in range(n)]
        lis=[i for i in range(1,n**2+1)]
        count=0
        row=0
        for j in range(n*2-1):
            if (row+1)*4==count:
                row+=1
            for i in range(len(matrix[0])):
                if matrix[row][i]!=0:
                    pass
                else:
                    matrix[row][i]=lis.pop(0)
            count+=1
            matrix=self.clockwise(matrix)
        while matrix[0][0]!=1:
            matrix=self.clockwise(matrix)


        return matrix
    def clockwise(self,a):
        b=[list(row) for row in list(zip(*a))][::-1]
        return b



if __name__ == '__main__':
    a=Solution()
    pprint.pprint(a.generateMatrix(10))