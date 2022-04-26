from typing import Optional

from tree.TreeNode import TreeNode


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
        self.res=0
        self.rank=0
        def traverse(root,k):
            if not root:
                return
            traverse(root.left,k)
            self.rank=self.rank+1
            if self.rank==k:
                self.res=root.val
                return
            traverse(root.right,k)



