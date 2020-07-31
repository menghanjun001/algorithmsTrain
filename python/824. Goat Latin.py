class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        lis=S.split(' ')
        for i in range(len(lis)):
            if lis[i][0] in 'aeiouAEIOU':
                lis[i]=lis[i]+'ma'+'a'*(i+1)
            else:
                lis[i]=(lis[i]+lis[i][0]+'ma'+'a'*(i+1))[1:]
        return ' '.join(lis)
if __name__ == '__main__':
    a=Solution()
    print(a.toGoatLatin("I speak Goat Latin"))