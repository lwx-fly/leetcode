from listnode.ListNode import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 1 -> 2 -> 3 ->4
        # 0->2 ,1->3
        # ListNode start = temp.next; 1
        # ListNode end = temp.next.next;  2

        # temp.next = end;0->2
        # start.next = end.next; 1->3
        # end.next = start;2->1
        # temp = start;
        # pre -> head -> next->后
        if not head or not head.next:
            return head
        next = head.next
        head.next = self.swapPairs(next.next)
        next.next = head
        return next
