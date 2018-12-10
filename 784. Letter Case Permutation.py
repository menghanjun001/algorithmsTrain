class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res=[]
        self.dfs(S,0,'',res)
        return res

    def dfs(self, S, pos, s, res):
        if pos==len(S):
            res.append(s)
            return
        if S[pos].isalpha():
            self.dfs(S,pos+1,s+S[pos].lower(),res)
            self.dfs(S,pos+1,s+S[pos].upper(),res)
        else:
            self.dfs(S,pos+1,s+S[pos],res)


if __name__ == '__main__':
    a=Solution()
    print(a.letterCasePermutation('a1b1'))