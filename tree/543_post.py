from tree.TreeNode import TreeNode

'''
二叉树直径
后序遍历
'''
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        def deep(root):
            if not root:
                return 0
            left = deep(root.left)
            right = deep(root.right)
            a = left + right
            self.ans = max(self.ans, a)
            return max(left, right) + 1
        deep(root)
        return self.ans
