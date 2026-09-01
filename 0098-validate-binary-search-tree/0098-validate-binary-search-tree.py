# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        
        def check(node, low, high):
            if node is None:
                return True

            # Node must be strictly between low and high
            if node.val <= low or node.val >= high:
                return False

            # Left subtree: values must be smaller
            # Right subtree: values must be greater
            return (check(node.left, low, node.val) and
                    check(node.right, node.val, high))

        return check(root, float("-inf"), float("inf"))