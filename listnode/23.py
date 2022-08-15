import heapq
from typing import Optional, List

from listnode.ListNode import ListNode


class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        h = dummy
        res = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(res, (lists[i].val, i))
                lists[i] = lists[i].next

        while res:
            val, idx = heapq.heappop(res)
            h.next = ListNode(val)
            h = h.next

            if lists[idx]:
                heapq.heappush(res, (lists[idx].val, idx))
                lists[idx] = lists[idx].next

        return dummy.next
