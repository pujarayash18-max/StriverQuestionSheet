# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        ans = []

        def dfs(node, level):
            if node is None:
                return

            # First node visited at this level
            if level == len(ans):
                ans.append(node.val)

            # Reverse preorder: Root -> Right -> Left
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 0)

        return ans