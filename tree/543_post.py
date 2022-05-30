from tree.TreeNode import TreeNode

'''
二叉树直径
后序遍历
二叉树直径为左右两个子树深度之和
'''
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res=0

        def deep(root):
            if not root:
                return 0
            left=deep(root.left)
            right=deep(root.right)
            self.res=max(self.res,left+right)
            return max(left,right)+1
        deep(root)
        return self.res
