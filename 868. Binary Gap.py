class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        maxLenght=0
        index=[]
        s=bin(N).replace('0b','')
        for i in range(len(s)):
            if s[i] == '1':
                index.append(i)
        if len(index)==1:
            return 0
        else:
            for i in range(1,len(index)):
                maxLenght=max(maxLenght,index[i]-index[i-1])
            return maxLenght
if __name__ == '__main__':
    a=Solution()
    print(a.binaryGap(3))