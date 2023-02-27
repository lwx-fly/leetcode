import collections
from typing import List

from tree.TreeNode import TreeNode

'''
从上到下打印二叉树
'''


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            #不需要按照层打印，不要加上循环
            node = queue.popleft()
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
