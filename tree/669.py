from typing import Optional

from tree.TreeNode import TreeNode


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val<low:
            return self.trimBST(root.right,low,high)
        elif root.val >high:
            return self.trimBST(root.left,low,high)
        left=self.trimBST(root.left,low,high)
        right=self.trimBST(root.right,low,high)
        root.left=left
        root.right=right
        return root