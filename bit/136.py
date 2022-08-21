from typing import List


class Solution:
    '''
    a ^ a = 0
    成对的数字会变成0
    0和其他数字异或还是他
    '''

    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^ i
        return res
