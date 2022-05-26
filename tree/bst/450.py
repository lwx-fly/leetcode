from typing import Optional

from tree.TreeNode import TreeNode

'''
删除二叉树中节点
'''


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def getMin(root):
            while root.left:
                root=root.left
            return root
        if not root:
            return None
        if root.val==key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            mid=getMin(root.right)
            root.right=self.deleteNode(root.right,mid.val)
            root.val=mid.val
        elif root.val < key:
            root.right=self.deleteNode(root.right,key)
        elif root.val > key:
            root.left=self.deleteNode(root.left,key)
        return root
