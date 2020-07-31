class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyset = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        lis=[]
        for i in keyset:
            i = set(i)
            # print(i)
            for word in words:
                if set(word.lower()).issubset(i):
                    lis.append(word)
        return lis
if __name__ == '__main__':
    a=Solution()
    print(a.findWords(["Hello","Alaska","Dad","Peace"]))
