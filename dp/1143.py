'''

最长公共子序列
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        memo = [[-1] * (n + 1) for i in range(m + 1)]

        def dp(s1, i, s2, j):
            if i == len(s1) or j == len(s2):
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            if s1[i] == s2[j]:
                memo[i][j] = 1 + dp(s1, i + 1, s2, j + 1)
            else:
                memo[i][j] = max(dp(s1, i + 1, s2, j), dp(s1, i, s2, j + 1))
            return memo[i][j]

        return dp(text1, 0, text2, 0)
