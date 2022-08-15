from typing import Optional

from tree.TreeNode import TreeNode

'''
Subtree of Another Tree
'''


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return not subRoot
        def same(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val !=q.val:
                return False
            return same(p.left,q.left) and same(p.right,q.right)
        if same(root,subRoot):
            return True
        return same(root.left,subRoot) or same(root.right,subRoot)
