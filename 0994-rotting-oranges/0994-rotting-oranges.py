from collections import deque

class Solution:
    def orangesRotting(self, grid):
        n = len(grid)
        m = len(grid[0])

        # Queue stores: (row, column, time)
        q = deque()

        # Visited array
        visited = [[0] * m for _ in range(n)]

        # Put all initially rotten oranges into the queue
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    visited[i][j] = 2

        max_time = 0

        # 4 directions: top, right, bottom, left
        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]

        while q:
            row, col, time = q.popleft()

            max_time = max(max_time, time)

            # Visit all 4 neighboring cells
            for i in range(4):
                nrow = row + drow[i]
                ncol = col + dcol[i]

                # Check valid position and fresh orange
                if (0 <= nrow < n and
                    0 <= ncol < m and
                    grid[nrow][ncol] == 1 and
                    visited[nrow][ncol] != 2):

                    # Mark as rotten/visited
                    visited[nrow][ncol] = 2

                    # It becomes rotten in the next unit of time
                    q.append((nrow, ncol, time + 1))

        # Check if any fresh orange was not rotten
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and visited[i][j] != 2:
                    return -1

        return max_time