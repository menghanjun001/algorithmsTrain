class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A=A.split(' ')
        B=B.split(' ')
        res=[]
        for i in A:
            if A.count(i)==1 and i not in B:
                res.append(i)
        for i in B:
            if B.count(i)==1 and i not in A:
                res.append(i)
        return res