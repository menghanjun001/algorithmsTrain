class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        res=[i for i in letters if i > target]
        return letters[0] if not res else res[0]