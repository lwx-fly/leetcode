from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        stack = []
        res = [0] * length
        for i in range(length - 1, -1, -1):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            else:
                res[i] = 0
            stack.append(i)
        return res
