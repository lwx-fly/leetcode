'''
获取公共子序列长度lcs
结果为m-lcs+n-lcs

'''


class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        memo = [[-1] * (n + 1) for i in range(m + 1)]

        def dp(str1, i, str2, j):
            if i == len(str1) or j == len(str2):
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            if str1[i] == str2[j]:
                memo[i][j] = dp(str1, i + 1, str2, j + 1) + 1
            else:
                memo[i][j] = max(dp(str1, i + 1, str2, j), dp(str1, i, str2, j + 1))
            return memo[i][j]

        lcs = dp(word1, 0, word2, 0)
        return m - lcs + n - lcs
