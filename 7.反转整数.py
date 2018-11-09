class Solution:
    # @staticmethod
    def reverse(self,x):
        if str(x)[0]=='-':
            s= '-'+str(x)[1:][::-1]
            x=int(s)
        else:
            x=int(str(x)[::-1])
        return x if -2**31<x<2**31 else 0 #防止溢出，代码的鲁棒性
# if __name__ == '__main__':
#     while(True):
#         ii=input()
#         a=Solution
#         print(a.reverse(ii))



