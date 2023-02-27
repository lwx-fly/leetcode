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
                # 注意这里
                if not node.left and not node.right:
                    return res
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res = res + 1
        return res
