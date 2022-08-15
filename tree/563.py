from typing import Optional

from tree.TreeNode import TreeNode

'''
二叉树的坡度
'''


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def build(root):
            if not root:
                return 0
            left = build(root.left)
            right = build(root.right)
            self.res = self.res + abs(left - right)
            return left + right + root.val

        build(root)
        return self.res
