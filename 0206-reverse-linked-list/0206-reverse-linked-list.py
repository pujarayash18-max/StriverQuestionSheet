# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next   
            curr.next = prev        
            prev = curr             
            curr = next_node        
        return prev
obj=Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

obj = Solution()
ans = obj.reverseList(head)
curr = ans
while curr:
    print(curr.val)
    curr = curr.next
print("None")