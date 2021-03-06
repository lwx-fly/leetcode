from typing import Optional

from tree.TreeNode import TreeNode

'''
二叉搜索树转成累加树
倒序
'''


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum=0
        def traverse(root):
            if not root:
                return
            traverse(root.right)
            self.sum=self.sum+root.val
            root.val=self.sum
            traverse(root.left)
        traverse(root)
        return root
