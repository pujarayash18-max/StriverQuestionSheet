# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def bstFromPreorder(self, preorder):

        index = [0]

        def build(lower, upper):
            if index[0] == len(preorder):
                return None

            value = preorder[index[0]]

            # Current value cannot belong to this subtree
            if value <= lower or value >= upper:
                return None

            # Create node
            root = TreeNode(value)
            index[0] += 1

            # Left: values must be smaller than root
            root.left = build(lower, value)

            # Right: values must be greater than root
            root.right = build(value, upper)

            return root

        return build(float('-inf'), float('inf'))