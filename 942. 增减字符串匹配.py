class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        low=0
        high=len(S)
        lis=[]
        for i in range(len(S)):
            if S[i] == 'I':
                lis.append(low)
                low+=1
            else:
                lis.append(high)
                high-=1
        lis.append(low)
        return lis