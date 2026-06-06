class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for row in matrix:
            row.reverse()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
solution = Solution()
solution.rotate(matrix)
print(matrix)