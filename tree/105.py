from typing import List

from tree.TreeNode import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(preorder, pre_start, pre_end, inorder, in_start, in_end):
            if pre_start > pre_end:
                return
            root_val = preorder[pre_start]
            index_ = inorder.index(root_val)
            left_len = index_ - in_start
            root = TreeNode(root_val)
            root.left = build(preorder, pre_start + 1, pre_start + left_len, inorder, in_start, index_ - 1)
            root.right = build(preorder, pre_start + left_len + 1, pre_end, inorder, index_ + 1, in_end)
            return root

        return build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
