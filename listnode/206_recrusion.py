from typing import Optional

from listnode import ListNode


#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        # 1 - >2 ->3 ->4  ---> 4->3->2
        h=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return h

