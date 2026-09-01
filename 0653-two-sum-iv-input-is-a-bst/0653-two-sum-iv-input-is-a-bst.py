# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root, k):

        inorder = []

        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)

        dfs(root)

        left = 0
        right = len(inorder) - 1

        while left < right:
            total = inorder[left] + inorder[right]

            if total == k:
                return True

            elif total < k:
                left += 1

            else:
                right -= 1

        return False