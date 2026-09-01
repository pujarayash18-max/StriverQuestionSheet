"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root):

        if root is None:
            return None

        level = root

        while level.left:
            current = level

            while current:
                # Connect left child to right child
                current.left.next = current.right

                # Connect across different parents
                if current.next:
                    current.right.next = current.next.left

                # Move to next node in the same level
                current = current.next

            # Move to the next level
            level = level.left

        return root
        