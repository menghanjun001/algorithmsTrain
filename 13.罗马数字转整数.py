class Solution:
    def romanToInt(self, s):
        d={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        sum=0
        for i in range(len(s)-1):
            if d[s[i]]<d[s[i+1]]:
                sum-=d[s[i]]
            else:
                sum+=d[s[i]]
        return sum+d[s[-1]]