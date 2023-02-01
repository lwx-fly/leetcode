from typing import List

from listnode import ListNode


class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre
