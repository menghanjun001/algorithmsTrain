class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.istitle() or word.isupper() or word.islower():
            return True
        else:
            return False