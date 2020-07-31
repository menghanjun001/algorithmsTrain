class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        distance = 0
        to = 1  # to=1 2 3 4 指向北东南西
        x = 0
        y = 0
        for command in commands:
            if command == -1:
                to = (to + 1) % 4
            elif command == -2:
                to = (to - 1) % 4
            else:
                for i in range(command):
                    if to == 1:
                        if [x, y + 1] not in obstacles:
                            y += 1

                        else:
                            break

                    elif to == 2:
                        if [x + 1, y] not in obstacles:
                            x += 1

                        else:
                            break
                    elif to == 3:
                        if [x, y - 1] not in obstacles:
                            y -= 1
                        else:
                            break

                    elif to == 0:
                        if [x - 1, y] not in obstacles:
                            x -= 1
                        else:
                            break
                    distance = max(distance, x ** 2 + y ** 2)

                    # print((x,y))
        return distance
if __name__ == '__main__':
    a=Solution()
    print(a.robotSim([4,-1,3],[]))