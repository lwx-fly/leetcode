from tree.TreeNode import TreeNode


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        m = max(nums)
        # m = max(nums)
        root = TreeNode(m)
        n = nums.index(m)
        root.left = self.constructMaximumBinaryTree(nums[:n])
        root.right = self.constructMaximumBinaryTree(nums[n + 1:])
        return root
