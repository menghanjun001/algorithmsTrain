class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.dfs(row, col, board, word, '',[]):
                    return True
        return False

    def dfs(self, row, col, board, word, temp,lis):
        if row < 0 or row > len(board)-1 or col < 0 or col > len(board[0])-1:
            return False
        # print(temp)
        # print(lis)
        if temp+board[row][col]==word and [row,col] not in lis:
            return True
        if temp == word[:len(temp)] and [row,col] not in lis:
            return self.dfs(row+1, col, board, word, temp+board[row][col],lis+[[row,col]])\
                   or self.dfs(row-1, col, board, word, temp+board[row][col],lis+[[row,col]])\
                   or self.dfs(row, col+1, board, word, temp+board[row][col],lis+[[row,col]])\
                   or self.dfs(row, col-1, board, word, temp+board[row][col],lis+[[row,col]])
        else:
            return

if __name__ == '__main__':
    a=Solution()
    print(a.exist([["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]],
"aaaaaaaaaaab"))