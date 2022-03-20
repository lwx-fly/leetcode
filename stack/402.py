class Solution:
    # Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
    # 1432219 k=3
    def removeKdigits(self, num: str, k: int) -> str:
        length = len(num)
        remain = length - k
        stack = []
        # 递增序列
        for i in num:
            while k and stack and i < stack[-1]:
                stack.pop()
                k = k - 1
            stack.append(i)
        return ''.join(stack[:remain]).lstrip('0') or '0'
