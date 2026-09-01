class Solution:
    def buildTree(self, preorder, inorder):

        index = {}

        for i in range(len(inorder)):
            index[inorder[i]] = i

        pre_index = [0]

        def build(left, right):

            if left > right:
                return None

            root_value = preorder[pre_index[0]]
            pre_index[0] += 1

            root = TreeNode(root_value)

            mid = index[root_value]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)