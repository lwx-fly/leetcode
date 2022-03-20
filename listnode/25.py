from typing import Optional
from listnode import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # recursion
        def reverse(head, tail):
            pre = None
            while head != tail:
                next = head.next
                head.next = pre
                pre = head
                head = next
            return pre

        if not head or not head.next:
            return head
        tail = head
        for i in range(k):
            if not tail:
                return head
            tail = tail.next
        h1 = reverse(head, tail)
        head.next = self.reverseKGroup(tail, k)
        return h1
