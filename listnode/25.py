from typing import Optional
from listnode import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, tail):
            # 1->2->3
            if not head or not head.next:
                return head
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
            #  3 21 h1.next=self.reverse.(tail
        # 1 2 3 4 5
        h1 = reverse(head, tail)
        head.next = self.reverseKGroup(tail, k)
        return h1
