from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        l = len(nums)
        res = [0] * (l)
        # 递减
        #环形数组
        for i in range(2 * l - 1, -1, -1):
            while stack and nums[i % l] >= stack[-1]:
                stack.pop()
            if stack:
                res[i % l] = stack[-1]
            else:
                res[i % l] = -1
            stack.append(nums[i % l])
        return res

    # 环形数组
