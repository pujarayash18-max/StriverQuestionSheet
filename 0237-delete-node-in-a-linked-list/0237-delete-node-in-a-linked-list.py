class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        node.val=node.next.val
        node.next=node.next.next
obj=Solution()

head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)
obj.deleteNode(head.next)
result = head
print("Head value:", result.val)
while result:
    print(result.val)
    result = result.next
        