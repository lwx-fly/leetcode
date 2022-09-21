import sys
from typing import List

'''
最小路径和
'''


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = [[-1] * (n + 1) for i in range(m + 1)]
        memo[0][0] = grid[0][0]
        # https://cdn.jsdelivr.net/gh/lwx-fly/img@master//img/image-20220919164729164.png
        for i in range(1, m):
            memo[i][0] = memo[i - 1][0] + grid[i][0]
        for j in range(1, n):
            memo[0][j] = memo[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] = min(memo[i - 1][j], memo[i][j - 1]) + grid[i][j]
        return memo[m - 1][n - 1]
