from listnode import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverseN(head, n):
            # 1->2->3->4->5 --- > 3->2->1->4
            if n == 1:
                # self.next = head.next
                return head
            cur = head.next.next
            last = reverseN(head.next, n - 1)
            head.next.next = head
            head.next = cur
            return last

        if left == 1:
            return reverseN(head, right)
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head
