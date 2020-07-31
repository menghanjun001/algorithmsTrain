# 1，整体思路是元素先依次进入栈1，再从栈1依次弹出到栈2，然后弹出栈2顶部的元素，整个过程就是一个队列的先进先出
# 2，但是在交换元素的时候需要判断两个栈的元素情况：
# “进队列时”，队列中是还还有元素，若有，说明栈2中的元素不为空，此时就先将栈2的元素倒回到栈1 中，保持在“进队列状态”。
# “出队列时”，将栈1的元素全部弹到栈2中，保持在“出队列状态”。
# 所以要做的判断是，进时，栈2是否为空，不为空，则栈2元素倒回到栈1，出时，将栈1元素全部弹到栈2中，直到栈1为空。

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stacka=[]
        self.stackb=[]
    def push(self, node):
        self.stackb.append(node)
    def pop(self):
        # return xx
        if self.stacka:         #如果栈a有结点，直接弹出
            return self.stacka.pop()

        else:                   #如果栈a无结点，栈b有结点,栈b弹到栈a里
            while self.stackb:
                self.stacka.append(self.stackb.pop())
            #pop()只执行一次，不写返回值while结束就无返回值了
            return self.stacka.pop()