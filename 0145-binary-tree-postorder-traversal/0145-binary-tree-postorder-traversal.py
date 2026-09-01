class Solution:
    def postorderTraversal(self, root):
        ans = []

        def postorder(node):
            if node is None:
                return

            # Left
            postorder(node.left)

            # Right
            postorder(node.right)

            # Root
            ans.append(node.val)

        postorder(root)

        return ans