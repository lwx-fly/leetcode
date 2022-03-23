from listnode.ListNode import ListNode


class Solution:
    # sort listNode
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # slow 为中点
        tmp = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(tmp)

        dummy = ListNode(0)
        h = dummy

        while left and right:
            if left.val < right.val:
                h.next = left
                left = left.next
            else:
                h.next = right
                right = right.next
            h = h.next
        if left:
            h.next = left
        else:
            h.next = right
        return dummy.next
