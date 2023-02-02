from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # x-> 下一个比x 大的数
        res = {}
        # 倒着遍历
        # 单调减
        stack = []
        for i in reversed(nums2):
            while stack and i > stack[-1]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            else:
                res[i] = -1
            stack.append(i)
        return [res[i] for i in nums1]
