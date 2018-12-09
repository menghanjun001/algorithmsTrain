from functools import reduce


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num in [i for i in range(10)]:
            return num
        else:
            lis=[]
            for i in range(len(str(num))):
                lis.append(int(str(num)[i]))

            return self.addDigits(reduce(lambda x,y:x+y,lis))
if __name__ == '__main__':
    a=Solution()
    print(a.addDigits(38))