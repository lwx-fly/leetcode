class Solution:
    '''
    是否是2的幂
    n & (n-1) 这个操作是算法中常见的，作用是消除数字 n 的二进制表示中的最后一个 1。
    '''

    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        return n & (n - 1) == 0
