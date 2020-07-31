class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1=0
        index2=len(numbers)-1
        while True:
            if numbers[index1]+numbers[index2]>target:
                index2-=1
            elif numbers[index1] + numbers[index2] < target:
                index1+=1
            else:
                return [index1+1,index2+1]