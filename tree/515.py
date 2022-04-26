from typing import List, Optional

from tree.TreeNode import TreeNode


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []

        def traverse(root, level):
            if not root:
                return
            if len(self.res<=level):
                self.res.append(root.val)
            else:
                self.res[level]=max(self.res[level],root.val)
            traverse(root.left, level + 1)
            traverse(root.right, level + 1)
        traverse(root, 0)
        return self.res

    # dfs
