
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [{} for i in range(9)]
        cols = [{} for i in range(9)]
        boxes = [{} for i in range(9)]
        for _i in range(9):
            for _j in range(9):
                num = board[_i][_j]
                if num != '.':
                    num = int(num)
                    boxIndex = (_i // 3) * 3 + _j // 3
                    rows[_i][num] = rows[_i].get(num, 0) + 1
                    cols[_j][num] = cols[_j].get(num, 0) + 1
                    boxes[boxIndex][num] = boxes[boxIndex].get(num, 0) + 1
                    if rows[_i][num] > 1 or cols[_j][num]>1 or boxes[boxIndex][num] > 1:
                        return False
        return True


if __name__ == '__main__':
    a = Solution()
    print(a.isValidSudoku([
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]))
