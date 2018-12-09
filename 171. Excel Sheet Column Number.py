import pprint


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        d=dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ',[i for i in range(1,27)]))
        pprint.pprint(d)
        sum=0
        s=s[::-1]
        for i in range(len(s)):
            sum+=d[s[i]]*((26)**i)

        return sum
if __name__ == '__main__':
    a=Solution()
    print(a.titleToNumber('AB'))