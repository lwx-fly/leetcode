from typing import Optional, List

from tree.TreeNode import TreeNode


def levelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    res = []
    self.level(root, 0, res)
    return res


def level(self, root, level, res):
    if not root: return
    if len(res) == level: res.append([])
    res[level].append(root.val)
    if root.left: self.level(root.left, level + 1, res)
    if root.right: self.level(root.right, level + 1, res)
