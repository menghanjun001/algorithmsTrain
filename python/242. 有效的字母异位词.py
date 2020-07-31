class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1={}
        d2={}
        for i in s:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1
        for i in t:
            if i not in d2:
                d2[i]=1
            else:
                d2[i]+=1
        if d1==d2:
            return True
        else:
            return False
if __name__ == '__main__':
    a=Solution()
    print(a.isAnagram('anaram','nagaram'))