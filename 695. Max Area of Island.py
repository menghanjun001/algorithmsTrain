import pprint


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxArea=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                print(row,col)
                if grid[row][col]==1:
                    maxArea=max(maxArea,self.dfs(row,col,grid))
                # pprint.pprint(grid)
                # print(maxArea)
        return maxArea
    def dfs(self, row, col,grid):
        if row<0 or row >=len(grid) or col <0 or col>=len(grid[0]):
            return 0
        if grid[row][col]==1:
            grid[row][col] = 9
            # print(row,col)
            return 1+self.dfs(row+1,col,grid)\
                   +self.dfs(row-1,col,grid)\
                   +self.dfs(row,col+1,grid)\
                   +self.dfs(row,col-1,grid)
        return 0
if __name__ == '__main__':
    a=Solution()
    print(a.maxAreaOfIsland([[0,1]]))