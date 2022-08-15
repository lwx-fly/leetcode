from typing import Optional

from listnode.ListNode import ListNode

'''
先分割成两个子数组，然后连接起来
'''


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        h1 = ListNode(0)
        h2 = ListNode(0)

        l1 = h1
        l2 = h2

        p = head

        while p:
            if p.val < x:
                l1.next = p
                l1 = l1.next
            else:
                l2.next = p
                l2 = l2.next
            tmp = p.next
            p.next = None
            p = tmp

        l1.next = h2.next
        return h1.next
