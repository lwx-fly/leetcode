from tree.TreeNode import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.recur(root) != -1

    def recur(self, root):
        if not root:
            return 0
        left = self.recur(root.left)
        if left == -1:
            return -1
        right = self.recur(root.right)
        if right == -1:
            return -1
        if abs(left - right) < 2:
            return max(left, right) + 1
        else:
            return -1
