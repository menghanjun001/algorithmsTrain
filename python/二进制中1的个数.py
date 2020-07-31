# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        return sum([(n>>i &1)for i in range(32)])
# 负数+2^32就可以得到负数的补码，计算机中都是以补码形式存储负数
# return bin(n).replace("0b","").count("1") if n>=0 else bin(2**32+n).replace("0b","").count("1")


# //超级简单容易理解                            //&(与)
# # // //把这个数逐次 右移 然后和1 与,
# # //就得到最低位的情况,其他位都为0,
# # //如果最低位是0和1与 之后依旧 是0，如果是1，与之后还是1。
# # //对于32位的整数 这样移动32次 就记录了这个数二进制中1的个数了 