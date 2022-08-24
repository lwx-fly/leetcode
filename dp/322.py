import sys
from typing import List

'''
零钱兑换
剪枝
'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 初始化memo数组，-2 代表未处理过
        memo = [-2] * [amount + 1]

        def dp(coins, amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            if memo[amount] != -2:
                return memo[amount]
            res = sys.maxsize
            for i in coins:
                sub = dp(coins, amount)
                if sub == -1:
                    continue
                res = min(res, sub + 1)
            if res == sys.maxsize:
                memo[amount] = -1
            else:
                memo[amount] = res
            return memo[amount]

        return dp(coins, amount)
