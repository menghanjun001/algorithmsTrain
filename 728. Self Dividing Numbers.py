class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res=[]
        for i in range(left,right+1):
            if self.judge(i):
                res.append(i)
        return res

    def judge(self, i):
        if '0' in str(i):
            return False
        for j in str(i):
            if i%int(j) !=0:
                return False
        return True
if __name__ == '__main__':
    a=Solution()
    print(a.selfDividingNumbers(1,22))