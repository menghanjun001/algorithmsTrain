class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        mos = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
               ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        passwd = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
        d = dict(zip(passwd, mos))
        trans=[]
        for word in words:
            s=''
            for alpha in word:
                s+=d[alpha]
            trans.append(s)
        return len(set(trans))
if __name__ == '__main__':
    a=Solution()
    print(a.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))