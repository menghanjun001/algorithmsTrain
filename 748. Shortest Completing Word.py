
from collections import Counter
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        a=''.join(l for l in licensePlate.lower() if l.isalpha())
        A=[w for w in words if all(Counter(w)[k]>=Counter(a)[k] for k in Counter(a))]

        return [w for w in A if len(w)==min(map(len,A))][0]

if __name__ == '__main__':
    a=Solution()
    print(a.shortestCompletingWord("GrC8950",
["measure","other","every","base","according","level","meeting","none","marriage","rest"]))