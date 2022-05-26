from typing import Optional

from tree.TreeNode import TreeNode

'''
验证二叉搜索树
'''

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root,min,max):
            if not root:
                return True
            if min and min.val >=root.val:
                return False
            if max and max.val <=root.val:
                return False
            return validate(root.left,min,root) and validate(root.right,root,max)
        return validate(root,None,None)

