from listnode import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 1-> 2 -> 3 -> 4 ->5  ---> 1 -> 4->3->2  -> 5
        # dummy head
        # first find left border left ,
        # then  find right border left
        # then stash right.next tmp
        # right.next=None
        # now you need reverse from left to right and get result from reverse
        # then left point to tmp
        # pre-> head1
        def reverse(head):
            pre = None
            while head:
                next = head.next
                head.next = pre
                pre = head
                head = next
            return pre

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(left - 1):
            pre = pre.next
        left_round = pre.next
        right_round =left_round
        print(left_round.val)
        for i in range(left, right):
            right_round = right_round.next

        tmp = right_round.next
        right_round.next = None
        h1 = reverse(left_round)
        pre.next = h1
        left_round.next = tmp
        return dummy.next
