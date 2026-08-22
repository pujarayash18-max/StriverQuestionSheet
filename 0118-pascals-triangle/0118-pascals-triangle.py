class Solution:
    def generate(self, numRows):
        result = []

        for N in range(1, numRows + 1):
            row = []
            value = 1
            row.append(value)

            for i in range(1, N):
                value = value * (N - i)
                value = value // i
                row.append(value)

            result.append(row)

        return result