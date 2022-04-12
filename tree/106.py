from typing import List

from tree.TreeNode import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(inorder, in_start, in_end, postorder, post_start, post_end):
            if in_start > in_end:
                return None
            root_ = postorder[post_end]
            index_ = inorder.index(root_)
            left_len = index_ - in_start
            root = TreeNode(root_)
            root.left = build(inorder, in_start, index_ - 1, postorder, post_start, post_start + left_len - 1)
            root.right = build(inorder, index_ + 1, in_end, postorder, post_start + left_len, post_end - 1)
            return root

        return build(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)
