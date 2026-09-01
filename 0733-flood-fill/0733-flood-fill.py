class Solution:
    def floodFill(self, image, sr, sc, color):

        original = image[sr][sc]

        # Already the required color
        if original == color:
            return image

        rows = len(image)
        cols = len(image[0])

        def dfs(r, c):

            # Change current pixel
            image[r][c] = color

            # 4 directions
            directions = [
                (-1, 0),  # up
                (1, 0),   # down
                (0, -1),  # left
                (0, 1)    # right
            ]

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # Check boundaries and original color
                if (0 <= nr < rows and
                    0 <= nc < cols and
                    image[nr][nc] == original):

                    dfs(nr, nc)

        dfs(sr, sc)

        return image