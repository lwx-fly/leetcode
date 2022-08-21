class Solution:

    '''
    一的个数
    '''

    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            n = n & (n - 1)
            res = res + 1
        return res
