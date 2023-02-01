from listnode import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverse(head, n):
            if n == 1:
                return head
            h = reverse(head.next, n - 1)
            cur = head.next.next
            head.next.next = head
            head.next = cur
            return h

        if left == 1:
            return reverse(head, right)
        # 1 2 3 4 5  , [3, 4 ]
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head
