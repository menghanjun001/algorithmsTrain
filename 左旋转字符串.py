# -*- coding:utf-8 -*-
class Solution:
    @classmethod
    def LeftRotateString(cls, s, n):
        # write code here
        if n<0:
            return None
        else:
            return s[n:]+s[:n]