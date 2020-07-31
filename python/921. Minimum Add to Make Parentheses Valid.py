class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack=[]
        count=0
        for i in S:
            if stack and stack[-1]=='(' and i==')':
                stack.pop()
                count-=1
            else:
                stack.append(i)
                count+=1
        return count
if __name__ == '__main__':
    a=Solution()
    print(a.minAddToMakeValid("()))(("))