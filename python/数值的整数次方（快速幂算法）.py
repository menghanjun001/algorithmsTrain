# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code
        if base==0:
            return 0
        if exponent==0:
            return 1
        e=abs(exponent)
        res=1
        while e>0:
            if e&1==1:
                res=res*base
            e>>=1
            base*=base
        return res if exponent>0 else 1/res
