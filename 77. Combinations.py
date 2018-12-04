class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(n,k,0,[],res)
        return res

    def dfs(self, n, k, start, temp, res):
        if k==0:
            res.append(temp)
            return
        for i in range(start+1,n+1):
            self.dfs(n,k-1,i,temp+[i],res)


if __name__ == '__main__':
    a=Solution()

    print(a.combine(4,2))
# a=[1,2]
# def add(x):
#     x.append(3)
#     return
# add(a)
# print(a) #a=[1, 2, 3]