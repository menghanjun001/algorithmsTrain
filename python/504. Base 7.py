class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        res=[]
        if num==0:
            return '0'
        if num<0:
            num=-num
            while num!=0:
                mod=num%7
                res.append(str(mod))
                num=(num-mod)//7
            return '-'+''.join(res[::-1])
        else:
            while num!=0:
                mod=num%7
                res.append(str(mod))
                num=(num-mod)//7
            return ''.join(res[::-1])