from typing import Optional

from tree.TreeNode import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def getMin(node):
            if node.left:
                node=node.left
            return node
        if not root:return None
        if root.val==key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            mid=getMin(root)
            root.right=self.deleteNode(root.right,key)
            root.val=mid.val
        elif root.val> key:
            self.deleteNode(root.left,key)
        elif root.val< key:
            self.deleteNode(root.right,key)
        return root


