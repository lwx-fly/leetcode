'''
Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:

Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:

Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
Constraints:

1 <= s1.length, s2.length <= 1000
s1 and s2 consist of lowercase English letters.
Related Topics
String
Dynamic Programming

👍 2194
👎 66

'''


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        memo = [[-1] * (n + 1) for i in range(m + 1)]

        def dp(str1, i, str2, j):
            res = 0
            if i == len(str1):
                for k in range(j, len(str2)):
                    res = res + ord(str2[k])
                return res
            if j == len(str2):
                for k in range(i, len(str1)):
                    res = res + ord(str1[k])
                return res
            if memo[i][j] != -1:
                return memo[i][j]
            if str1[i] == str2[j]:
                memo[i][j] = dp(str1, i + 1, str2, j + 1)
            else:
                memo[i][j] = min(dp(str1, i + 1, str2, j) + str1[i], dp(str1, i, str2, j + 1) + str2[j])
            return memo[i][j]

        return dp(s1, m, s2, n)
