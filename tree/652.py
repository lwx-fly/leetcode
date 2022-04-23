from typing import Optional, List

from tree.TreeNode import TreeNode


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # first serial subtree and then compare
        map = {}
        res = []

        def traverse(root: Optional[TreeNode], map, res):
            if not root:
                return "#"
            left = traverse(root.left, map, res)
            right = traverse(root.right, map, res)
            sub_tree = left + ',' + right + ',' + str(root.val)
            a = map.setdefault(sub_tree, 0)
            if a == 1:
                res.append(root)
            map[sub_tree] = a + 1
            return sub_tree

        traverse(root, map, res)
        return res
