from typing import List

from tree.TreeNode import TreeNode


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        def build(preorder, pre_start, pre_end, postorder, post_start, post_end):
            if pre_start > pre_end:
                return None
            if pre_start == pre_end:
                return TreeNode(preorder[pre_start])
            root_ = preorder[pre_start]
            left_root_ = preorder[pre_start + 1]
            index_ = postorder.index(left_root_)
            left_len = index_ - post_start + 1
            root = TreeNode(root_)
            root.left = build(preorder, pre_start + 1, pre_start + left_len, postorder, post_start,
                              index_)
            root.right = build(preorder, pre_start + left_len + 1, pre_end, postorder, index_ + 1, post_end - 1)
            return root
        return build(preorder, 0, len(preorder) - 1, postorder, 0, len(postorder) - 1)
