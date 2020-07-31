from collections import Counter


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d=Counter(s)
        lis=sorted(d.items(),key=lambda d:d[1])[::-1]
        s=''
        for i in lis:
            s+=i[0]*i[1]
        return s
if __name__ == '__main__':
    a=Solution()
    print(a.frequencySort("leanglkesanglanlkgnekg"))
