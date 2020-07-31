# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        return self.Help(sequence)
    def Help(self,sequence):
        if not sequence:
            return True
        root=sequence[-1]
        for i in range(len(sequence)):
            if sequence[i]>root:
                break
        for j in range(i, len(sequence)-1):
            if sequence[j]<root:
                return False
        left=self.Help(sequence[:i])
        right=self.Help(sequence[i:len(sequence)-1])
        return left and right
