class Solution:
    @staticmethod
    def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ''
        res=''
        for each in zip(*strs):
            if len(set(each))==1:
                res+=each[0]
            else:
                return res
        return res

# if __name__ == '__main__':
#
#     b=Solution()
#     print(b.longestCommonPrefix(["flower","flow","flight"]))


