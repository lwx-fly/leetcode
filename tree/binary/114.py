from typing import Optional

from tree.TreeNode import TreeNode


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return root
        # flattern left and right
        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left
        right = root.right

        root.left = None
        root.right = left
        p = root
        while p.right:
            p = p.right
        p.right = right
