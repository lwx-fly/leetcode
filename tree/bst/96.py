
'''
不同二叉搜索树的数量
'''


class Solution:
    def numTrees(self, n: int) -> int:
        memo = [[0] * (n + 1) for i in range(n + 1)]

        def count(low, high):
            if low > high:
                return 1
            if memo[low][high] != 0:
                return memo[low][high]
            res = 0
            for i in range(low, high + 1):
                left = count(low, i - 1)
                right = count(i + 1, high)
                res = res + left * right
            memo[low][high] = res
            return res

        res = count(1, n)
        return res
