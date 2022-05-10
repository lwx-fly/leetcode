from typing import List

from tree.TreeNode import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        def build(low, high):
            res = []
            if low > high:
                res.append(None)
                return res
            for i in range(low, high + 1):
                left = build(low, i - 1)
                right = build(i + 1, high)
                for j in left:
                    for k in right:
                        node = TreeNode(i)
                        node.left = j
                        node.right = k
                        res.append(node)
            return res

        return build(1, n)
