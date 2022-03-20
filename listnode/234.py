from listnode import ListNode


class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        def reverse(head):
            if head is None or head.next is None:
                return head
            h = reverse(head.next)
            head.next.next = head
            head.next = None
            return h

        slow = head
        fast = head
        k = 0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            k = k + 1
        # slow 为中点
        h1 = reverse(slow)
        for i in range(k):
            if head.val != h1.val:
                return False
            h1 = h1.next
            head = head.next
        return True
