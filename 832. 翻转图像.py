class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            A[i]=A[i][::-1]
            for j in range(len(A[i])):
                A[i][j]=A[i][j]^1
        return A

if __name__ == '__main__':
    a=Solution()
    print(a.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))