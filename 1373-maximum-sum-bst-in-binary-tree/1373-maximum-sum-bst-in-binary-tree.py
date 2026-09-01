# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def maxSumBST(self, root):

        self.max_sum = 0

        def postorder(node):
            if node is None:
                # Empty tree is a valid BST
                return float('inf'), float('-inf'), 0, True

            # Get information from left and right
            left_min, left_max, left_sum, left_bst = postorder(node.left)
            right_min, right_max, right_sum, right_bst = postorder(node.right)

            # Check whether current subtree is a BST
            if (left_bst and right_bst and
                left_max < node.val < right_min):

                current_sum = left_sum + node.val + right_sum

                self.max_sum = max(self.max_sum, current_sum)

                current_min = min(left_min, node.val)
                current_max = max(right_max, node.val)

                return current_min, current_max, current_sum, True

            # Current subtree is not a BST
            return 0, 0, 0, False

        postorder(root)

        return self.max_sum
        