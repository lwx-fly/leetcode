from listnode.ListNode import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        h1 = dummy
        while dummy.next and dummy.next.next:
            begin = dummy.next
            end = dummy.next.next

            dummy.next = end
            begin.next = end.next
            end.next = begin
            dummy = begin
        return h1.next
