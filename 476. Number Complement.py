class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return (int(''.join(map(str, [int(i) ^ 1 for i in bin(num).replace('0b', '')])), 2))
# print([int(i)^1 for i in str(101)])
