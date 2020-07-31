class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        S=self.backspace(S)
        T=self.backspace(T)
        if S==T:
            return True
        return False

    def backspace(self, S):
        stackA=[]
        for i in S:
            if i!='#':
                stackA.append(i)
            elif i=='#' and stackA:
                stackA.pop()
        return ''.join(stackA)


if __name__ == '__main__':
    a=Solution()
    print(a.backspace('ab##d'))
    print(a.backspace('c#d#'))