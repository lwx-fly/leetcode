import sys
from typing import List

'''
The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Return the knight's minimum initial health so that he can rescue the princess.

Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

Example 1:


Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output: 7
Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.
Example 2:

Input: dungeon = [[0]]
Output: 1
Constraints:

m == dungeon.length
n == dungeon[i].length
1 <= m, n <= 200
-1000 <= dungeon[i][j] <= 1000
Related Topics
Array
Dynamic Programming
Matrix

👍 4585
👎 83

'''


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        memo = [[-1] * (n + 1) for i in range(m + 1)]

        def dp(dungeon, i, j):
            m = len(dungeon)
            n = len(dungeon)
            if i == m - 1 and j == n - 1:
                if dungeon[i][j] < 0:
                    return -dungeon[i][j] + 1
                return 1
            if i == m or j == n:
                return sys.maxsize
            if memo[i][j] != -1:
                return memo[i][j]
            res = min(dp(dungeon, i + 1, j), dp(dungeon, i, j + 1)) - dungeon[i][j]
            if res < 0:
                memo[i][j] = 1
            else:
                memo[i][j] = res
            return memo[i][j]

        return dp(dungeon, 0, 0)
