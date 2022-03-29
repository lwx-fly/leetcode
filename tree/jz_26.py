from tree.TreeNode import TreeNode


class Solution:

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        return bool( A and  B) and (
                self.recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))

    def recur(self, A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return self.recur(A.left, B.left) and self.recur(A.right, B.right)
