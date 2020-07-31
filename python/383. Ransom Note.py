from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d=Counter(magazine)
        print(d)
        for i in ransomNote:
            if i not in d:
                return False
            if d[i]>=1:
                d[i]-=1
            else:
                return False
        return True
if __name__ == '__main__':
    a=Solution()
    print(a.canConstruct('aa','ab'))