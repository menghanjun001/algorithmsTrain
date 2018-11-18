import random
import time


def usingTime(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print('用时{}s'.format(end-start))
        return result
    return wrapper


class Solution(object):
    @usingTime
    def insertSort(self,array):
        for i in range(len(array)):
            for j in range(i):
                if array[i]<array[j]:
                    array[i],array[j]=array[j],array[i]

        return array

    @usingTime
    def bubbleSort(self,array):
        for i in range(len(array)):
            for j in range(1,len(array)-i):
                if array[j]<array[j-1]:
                    array[j-1],array[j]=array[j],array[j-1]
        return array

    @usingTime
    def quickSort(self,array):
        if not array:
            return []
        pivot=array[0]
        left=self.quickSort([i for i in array[1:] if i < pivot])
        right=self.quickSort([i for i in array[1:] if i >= pivot])

        return left+[pivot]+right
    @usingTime
    def bucketSort(self,array):
        bucket=[0]*20001
        sortNums=[]
        for i in array:
            bucket[i]+=1
        for j in range(len(bucket)):
            if bucket[j]!=0:
                for jj in range(bucket[j]):
                    sortNums.append(j)
        return sortNums



if __name__ == '__main__':
    a=Solution()
    b=[]
    for i in range(10000):
        b.append(random.randint(0,20000))
    print(b)
    # print(a.insertSort(b))
    # print(a.bubbleSort(b))
    # print(a.quickSort(b))
    print(a.bucketSort(b))
