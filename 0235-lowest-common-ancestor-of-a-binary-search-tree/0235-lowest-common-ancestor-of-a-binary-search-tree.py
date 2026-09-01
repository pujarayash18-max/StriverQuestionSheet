# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):

        while root:
            
            # Both nodes are smaller than root
            if p.val < root.val and q.val < root.val:
                root = root.left

            # Both nodes are greater than root
            elif p.val > root.val and q.val > root.val:
                root = root.right

            # They are on different sides
            # or root is p or q
            else:
                return root
        