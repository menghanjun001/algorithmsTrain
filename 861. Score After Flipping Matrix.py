import pprint


class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        pprint.pprint(A)
        for i in range(len(A)):
            if A[i][0]==0:
                A[i]=[1-j for j in A[i]]

        ret=0
        for i in range(len(A[0])):
            col=[A[j][i] for j in range(len(A))]
            print(col)
            ret+= max(sum(col),len(A)-sum(col))*(2**(len(A[0])-i-1))
        return ret
if __name__ == '__main__':
    a=Solution()
    print(a.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))