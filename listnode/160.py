from listnode.ListNode import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        x = headA
        y = headB
        while x != y:
            if x:
                x = x.next
            else:
                x = headB
            if y:
                y = y.next
            else:
                y = headA
        return x
