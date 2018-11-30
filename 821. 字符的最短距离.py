class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        index=[]
        lis=[]
        for i in range(len(S)):
            if S[i]==C:
               index.append(i)
        for i in range(len(S)):
            lis.append(min(map(lambda x:abs(x-i),index)))
        return lis
if __name__ == '__main__':
    a=Solution()
    print(a.shortestToChar("loveleetcode",'e'))
