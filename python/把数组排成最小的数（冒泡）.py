# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        numbers=list(map(str,numbers))
        for i in range(len(numbers)):
            for j in range(1,len(numbers)-i):
                if numbers[j-1]+numbers[j]>numbers[j]+numbers[j-1]:
                    numbers[j-1],numbers[j]=numbers[j],numbers[j-1]
        return ''.join(numbers)
