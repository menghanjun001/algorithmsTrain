class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        hashmap={'U':0,'D':0,'L':0,'R':0}
        for i in moves:
            hashmap[i]+=1
        if hashmap['U']==hashmap['D'] and hashmap['L']==hashmap['R']:
            return True
        return False