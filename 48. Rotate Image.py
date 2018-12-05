class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[:]=[list(row)[::-1] for row in zip(*matrix)]
        # return matrix
if __name__ == '__main__':
    a=Solution()
    print(a.rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
]))