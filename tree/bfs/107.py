import collections
from typing import List, Optional

from tree.TreeNode import TreeNode

'''
二叉树层序遍历
自底向上返回
'''
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if not root:
            return res
        q=collections.deque()
        q.append(root)
        while q:
            res1=[]
            l=len(q)
            for i in range(l):
                node=q.popleft()
                res1.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(res1)
        return list(reversed(res))
