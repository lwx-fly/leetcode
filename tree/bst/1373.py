import sys
from typing import Optional

from tree.TreeNode import TreeNode

'''
二叉搜素子树的最大键值和
'''

class Solution:

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0

        def traverse(root: Optional[TreeNode]):
            if not root:
                return (1, sys.maxsize, -sys.maxsize + 1, 0)
            left = traverse(root.left)
            right = traverse(root.right)
            res = [0] * 4
            # 0 bst 1 min 2 max 3sum
            if left[0] == 1 and right[0] == 1 and left[2] < root.val and right[1] > root.val:
                res[0] = 1
                res[1] = min(left[1], root.val)
                res[2] = max(right[2], root.val)
                res[3] = left[3] + right[3] + root.val
                self.max_sum = max(self.max_sum, res[3])
            else:
                res[0] = 0
            return res

        traverse(root)
        return self.max_sum
