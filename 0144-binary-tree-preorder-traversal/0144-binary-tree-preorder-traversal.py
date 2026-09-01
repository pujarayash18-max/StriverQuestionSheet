# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        ans = []

        def preorder(node):
            if node is None:
                return

            # Root
            ans.append(node.val)

            # Left
            preorder(node.left)

            # Right
            preorder(node.right)

        preorder(root)

        return ans