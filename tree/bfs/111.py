import collections

from tree.TreeNode import TreeNode


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 1
        q = collections.deque()
        q.append(root)
        while q:
            l = len(q)
            for i in range(l):
                node = q.popleft()
                if not node.left and not node.right:
                    return res
                if not node.left:
                    q.append(node.left)
                if not node.right:
                    q.append(node.right)
            res=res+1
        return res
