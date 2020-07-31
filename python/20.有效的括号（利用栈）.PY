class Solution:
    @classmethod
    def isValid(cls, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==0:
            return True
        if len(s)%2==1 or (s[0]==')' or s[0]=='}' or s[0]==']'):
            return False

        d={'}':'{',')':'(',']':'['}
        stack=[]
        for i in s:
            if i in d and d[i]==stack[-1]:

                stack.pop()
            else:
                stack.append(i)
        return True if len(stack)==0 else False

if __name__ == '__main__':
    a=Solution
    print(a.isValid(''))
