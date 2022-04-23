from tree.TreeNode import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 前序遍历
        self.ans = 0

        def traverse(root):
            if not root:
                return
            left = deep(root.left)
            right = deep(root.right)
            a = left + right
            self.ans = max(a, self.ans)
            traverse(root.left)
            traverse(root.right)

        def deep(root):
            if not root:
                return 0
            left = deep(root.left)
            right = deep(root.right)
            return max(left, right) + 1

        traverse(root)
        return self.ans
