class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cost=grid

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row==0 and col != 0:
                    cost[row][col]=cost[row][col-1]+grid[row][col]
                elif row != 0 and col == 0:
                    cost[row][col] =cost[row-1][col]+grid[row][col]
                elif row != 0 and col != 0:
                    cost[row][col]=min(cost[row][col-1],cost[row-1][col])+grid[row][col]
                # print(row, col, cost[row][col])
        return cost[-1][-1]

if __name__ == '__main__':
    a=Solution()
    print(a.minPathSum([[1]]))