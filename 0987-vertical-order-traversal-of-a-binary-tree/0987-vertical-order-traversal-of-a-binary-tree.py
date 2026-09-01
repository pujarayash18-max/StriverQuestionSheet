class Solution:
    def verticalTraversal(self, root):

        mp = {}

        # queue using a normal list
        q = [(root, 0, 0)]
        i = 0

        while i < len(q):

            node, row, col = q[i]
            i += 1

            if col not in mp:
                mp[col] = []

            mp[col].append((row, node.val))

            if node.left:
                q.append((node.left, row + 1, col - 1))

            if node.right:
                q.append((node.right, row + 1, col + 1))

        ans = []

        # columns from left to right
        for col in sorted(mp):

            # sort by row, then by value
            mp[col].sort()

            temp = []

            for row, value in mp[col]:
                temp.append(value)

            ans.append(temp)

        return ans