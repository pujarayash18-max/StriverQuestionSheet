# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root):

        ans = [float('-inf')]

        def solve(node):

            if node is None:
                return 0

            left = max(0, solve(node.left))
            right = max(0, solve(node.right))

            # Path passing through current node
            ans[0] = max(ans[0], left + node.val + right)

            # Return one side to parent
            return node.val + max(left, right)

        solve(root)

        return ans[0]