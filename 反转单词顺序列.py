# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        lst=s.split(' ')
        s=' '.join(lst[::-1])
        return s