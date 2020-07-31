class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        lis=[]
        while(matrix):
            lis.extend(matrix.pop(0))
            matrix=self.clockwise(matrix)
        return lis
    def clockwise(self,a):
        b=[list(row) for row in list(zip(*a))][::-1]
        return b
if __name__ == '__main__':
    a=Solution()
    print(a.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))