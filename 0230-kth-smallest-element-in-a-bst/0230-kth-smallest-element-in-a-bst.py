# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k):
        stack = []
        current = root
        count = 0

        while True:
            # Go as far left as possible
            while current is not None:
                stack.append(current)
                current = current.left

            # Visit node
            current = stack.pop()
            count += 1

            # kth smallest found
            if count == k:
                return current.val

            # Move to right subtree
            current = current.right
        