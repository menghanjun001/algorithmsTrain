class Solution(object):
    def __init__(self):
        self.hashmap={}
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n not in self.hashmap:
            self.hashmap[n]=1
        else:
            return False

        sum=0
        for i in str(n):
            sum+=int(i)**2
        return self.isHappy(sum)
        #self.isHappy(sum)是错的

if __name__ == '__main__':
    a=Solution()
    print(a.isHappy(10))