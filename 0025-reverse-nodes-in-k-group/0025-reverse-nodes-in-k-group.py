class Solution:
    def reverseKGroup(self, head, k):
        
        def getKthNode(node, k):
            while node and k > 1:
                node = node.next
                k -= 1
            return node

        temp = head
        prev = None

        while temp:
            # Find kth node of current group
            kth = getKthNode(temp, k)

            # Less than k nodes remaining
            if kth is None:
                if prev:
                    prev.next = temp
                break

            # Save next group
            next_node = kth.next

            # Separate current k-group
            kth.next = None

            # Reverse current group
            prev_node = None
            curr = temp

            while curr:
                next_curr = curr.next
                curr.next = prev_node
                prev_node = curr
                curr = next_curr

            # First group -> update head
            if temp == head:
                head = kth
            else:
                # Connect previous group to current reversed group
                prev.next = kth

            # temp is now the last node of reversed group
            prev = temp

            # Move to next group
            temp = next_node

        return head