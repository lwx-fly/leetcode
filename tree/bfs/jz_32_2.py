import collections
from typing import List

from tree.TreeNode import TreeNode

'''
从按层打印二叉树
'''


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            l = len(q)
            res1 = []
            for i in range(l):
                a = q.popleft()
                res1.append(a.val)
                if a.left:
                    q.append(a.left)
                if a.right:
                    q.append(a.riht)
            res.append(res1)
        return res
