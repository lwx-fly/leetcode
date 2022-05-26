from listnode import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverseN(head, n):
            if n == 1:
                return head
            h = reverseN(head.next, n - 1)
            cur = head.next.next
            head.next.next = head
            head.next = cur
            return h

        if left == 1:
            return reverseN(head, right)
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head

