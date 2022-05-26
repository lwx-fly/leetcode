import sys
from typing import Optional

from tree.TreeNode import TreeNode

'''
最大路径和
后序遍历
'''


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res = -sys.maxsize + 1

        def oneSide(root):
            if not root:
                return 0
            left = max(0, oneSide(root.left))
            right = max(0, oneSide(root.right))
            path = left + right + root.val
            self.res = max(self.res, path)
            return max(left, right) + root.val

        oneSide(root)
        return self.res
