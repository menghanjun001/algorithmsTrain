class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        d={}
        countA=countB=0
        index=0
        for i in secret:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
            # print(secret[index])
            if secret[index]==guess[index]:
                countA+=1
            index+=1
        for i in guess:
            if i in d and d[i]!=0:
                # print(d[i])
                countB+=1
                d[i]-=1
        return str(countA)+'A'+str(countB-countA)+'B'
if __name__ == '__main__':
    a=Solution()
    print(a.getHint('1123','0111'))
