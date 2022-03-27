from tree.TreeNode import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.recur(root.left, root.right)

    def recur(self, left, right):
        if not left and not right:
            return True
        if not left or not right or left.val != right.val:
            return False
        return self.recur(left.left, right.right) and self.recur(left.right, right.left)