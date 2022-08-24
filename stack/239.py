import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        list = collections.deque()
        l = len(nums)
        res = [0] * (l - k + 1)

        for i in range(l):
            if i >= k and i - k >= list[0]:
                list.popleft()
            while list and nums[list[-1]] <= nums[i]:
                list.pop()
            list.append(i)
            if i - k + 1 >= 0:
                res[i - k + 1] = nums[list[0]]
        return res
