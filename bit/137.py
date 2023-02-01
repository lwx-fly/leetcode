from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # if two == 0:
        #     if n == 0:
        #         one = one
        #     if n == 1:
        #         one = ~one
        # if two == 1:
        #     one = 0

        #异或
        # if two == 0:
        #     one = one ^ n
        # if two == 1:
        #     one = 0

        # 与运算
        # one = one ^ n & ~two

        a = b = 0
        for i in nums:
            a = a ^ i & ~b
            b = b ^ i & ~a
        return a
