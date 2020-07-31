class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count=0
        m=len(grid)
        n=len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    # print(row,col)
                    count+=4
                    if row + 1 < m and grid[row+1][col] == 1:
                        # print(row,col)
                        count-=2
                    if col+1 < n and grid[row][col+1] ==1:
                        # print(row,col)
                        count-=2
                    print('----')
                    # print(neighbor)
        return count

if __name__ == '__main__':
    a=Solution()
    print(a.islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))
