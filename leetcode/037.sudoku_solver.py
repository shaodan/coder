class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row = [0] * 9
        column = [0] * 9
        grid = [0] * 9

        for i in xrange(9):
            print board[i]
            for j in xrange(9):
                if board[i][j] == '.':
                    continue
                row[i] += 1
                column[j] += 1
                grid[i/3*3+j/3] += 1

        print row
        print column
        print grid



s = Solution()
board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
board = map(list, board)
s.solveSudoku(board)
