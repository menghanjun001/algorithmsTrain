class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        for i in range(len(ghosts)):
            print(ghosts[i][0])
            if (abs(target[0]) + abs(target[1]) >= abs(ghosts[i][0] - target[0]) + abs(
                    ghosts[i][1] - target[1])):
                return False
        return True
if __name__ == '__main__':
    a=Solution()
    print(a.escapeGhosts([[1, 0], [0, 3]],[0,1]))