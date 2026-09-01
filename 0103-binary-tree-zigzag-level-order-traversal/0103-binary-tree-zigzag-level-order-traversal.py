# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root):

        if root is None:
            return []

        q = [root]
        ans = []
        flag = True

        while q:
            n = len(q)
            level = []

            for i in range(n):
                node = q.pop(0)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                if flag:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)

            ans.append(level)

            flag = not flag

        return ans