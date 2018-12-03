class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        cost=triangle
        for row in range(len(triangle)):
            for col in range(len(triangle[row])):
                if col==0 and row>0:
                    cost[row][col]=cost[row-1][col]+triangle[row][col]
                elif col==len(triangle[row])-1 and row>0:
                    cost[row][col] = cost[row - 1][col-1] + triangle[row][col]
                elif (col!=0 or col!=len(triangle[row])-1) and row>0:
                    cost[row][col]=min(cost[row-1][col-1],cost[row-1][col])+triangle[row][col]
        return min(cost[-1])

if __name__ == '__main__':
    a=Solution()
    print(a.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))