# -*- coding:utf-8 -*-
class Solution:
    @classmethod
    def IsPopOrder(cls, pushV, popV):
        # write code here
        stack=[]
        while popV:
            #如果压入栈中的首元素和序列第一位一样，则无需压入就抛掉
            if pushV and pushV[0] == popV[0]:
                pushV.pop(0)
                popV.pop(0)
            #如果序列有元素，则压入栈中
            elif pushV:
                stack.append(pushV.pop(0))
            #如果栈顶元素和序列第一位相等，则抛出
            elif stack[-1] == popV[0]:
                stack.pop(-1)
                popV.pop(0)
            #都不满足说明没什么好抛的，直接return False
            else:
                return False
        return True

s=Solution.IsPopOrder([1,2,3,4,5],[4,5,3,2,1])
print(s)

