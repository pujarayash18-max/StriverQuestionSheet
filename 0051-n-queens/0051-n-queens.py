class Solution(object):
    def solveNQueens(self, n):
        result = []

        # Create empty chessboard
        board = [["." for _ in range(n)] for _ in range(n)]

        def isSafe(row, col):
            # Check same column
            for i in range(row):
                if board[i][col] == "Q":
                    return False

            # Check upper-left diagonal
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # Check upper-right diagonal
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True

        def backtrack(row):
            # All queens are placed
            if row == n:
                result.append(["".join(r) for r in board])
                return

            # Try every column in this row
            for col in range(n):

                if isSafe(row, col):
                    # Place queen
                    board[row][col] = "Q"

                    # Move to next row
                    backtrack(row + 1)

                    # Backtrack: remove queen
                    board[row][col] = "."

        backtrack(0)

        return result
        