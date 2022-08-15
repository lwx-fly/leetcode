from typing import Optional
from listnode import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, tail):
            # 1->2->3
            if not head or head == tail or not head.next:
                return head
            h1 = head.next
            head.next = reverse(h1.next, tail)
            h1.next = head
            return h1

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
