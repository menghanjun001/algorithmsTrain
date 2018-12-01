class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count=0
        for i in range(1,N+1):
            if self.judgeGood(i):
                print(i)
                count+=1
        return count

    def judgeGood(self, i):
        if ('2' in str(i) or '5'in str(i)  or '6' in str(i)or '9' in str(i) )and ('3' not in str(i) and '4' not in str(i) and '7' not in str(i)):
            return True
        else:
            return False
if __name__ == '__main__':
    a=Solution()
    print(a.rotatedDigits(20))
