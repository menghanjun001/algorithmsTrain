class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        sisterGetKinds=len(candies)/2
        kinds=len(set(candies))
        return min(sisterGetKinds,kinds)