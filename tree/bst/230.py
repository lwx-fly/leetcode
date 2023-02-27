from typing import Optional

from tree.TreeNode import TreeNode


'''
二叉搜索子树的最小k个元素
'''

class Solution:
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     self.res = []
    #     def traverse(root):
    #         if not root:
    #             return
    #         self.res.append(root.val)
    #         traverse(root.left)
    #         traverse(root.right)
    #     traverse(root)
    #     self.res.sort()
    #     if k > len(self.res):
    #         return None
    #     return self.res[k]
        def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
            self.rank=0
            self.res=0
            if not root:
                return 0
            def build(root,k):
                if not root:
                    return
                build(root.left,k)
                self.rank=self.rank+1
                if self.rank==k:
                    self.res=root.val
                    return
                build(root.right,k)
            build(root,k)
            return self.res


