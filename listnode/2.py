from typing import Optional

from listnode import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        flag = 0
        h = ListNode(0)
        h1 = h
        while l1 and l2:
            a = l1.val + l2.val + flag
            if a >= 10:
                flag = 1
                a = a % 10
            else:
                flag = 0
            l1 = l1.next
            l2 = l2.next
            h.next = ListNode(a)
            h = h.next

        while l1:
            a = l1.val + flag
            if a >= 10:
                flag = 1
                a = a % 10
            else:
                flag = 0
            h.next = ListNode(a)
            l1 = l1.next
            h = h.next
        while l2:
            a = l2.val + flag
            if a >= 10:
                flag = 1
                a = a % 10
            else:
                flag = 0
            h.next = ListNode(a)
            l2 = l2.next
            h = h.next
        if flag > 0:
            h.next = ListNode(flag)
        return h1.next
