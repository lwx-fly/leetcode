from typing import Optional

from tree.TreeNode import TreeNode


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        #
        if not root:
            return root
        # flattern left and right
        self.flatten(root.left)
        self.flatten(root.right)
        #   1
        # 2   3
        #4 5 6 7
        left = root.left
        right = root.right

        root.left = None
        root.right = left
        p = root
        while p.right:
            p = p.right
        p.right = right
