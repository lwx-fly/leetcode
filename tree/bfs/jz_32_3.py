import collections
from typing import List

from tree.TreeNode import TreeNode

'''
从按层Z字打印二叉树
'''


def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root: return []
    res, deque = [], collections.deque([root])
    while deque:
        tmp = collections.deque()
        for _ in range(len(deque)):
            node = deque.popleft()
            if len(res) % 2:
                tmp.appendleft(node.val)  # 偶数层 -> 队列头部
            else:
                tmp.append(node.val)  # 奇数层 -> 队列尾部
            if node.left: deque.append(node.left)
            if node.right: deque.append(node.right)
        res.append(list(tmp))
    return res
