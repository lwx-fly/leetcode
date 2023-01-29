from typing import Optional

from listnode.ListNode import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        h1 = dummy

        while list1 and list2:
            if list1.val > list2.val:
                node1 = ListNode(list2.val)
                dummy.next = node1
                dummy = dummy.next
                list2 = list2.next
            else :
                node1 = ListNode(list1.val)
                dummy.next = node1
                dummy = dummy.next
                list1 = list1.next
        if list1:
            dummy.next=list1
        if list2:
            dummy.next=list2
        return h1.next