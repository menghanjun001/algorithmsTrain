# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        h=[0]*256
        for i in s:
            h[ord(i)]+=1
        for j in range(len(s)):
            if h[ord(s[j])]==1:
                return j
        return -1
