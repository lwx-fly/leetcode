'''
序列化和反序列化树
使用后序遍历
'''
import collections

from tree.TreeNode import TreeNode


class Codec:

    def serialize(self, root):
        self.res = ""

        def build(root):
            if not root:
                self.res = self.res + "#,"
                return
            build(root.left)
            build(root.right)
            self.res = self.res + str(root.val) + ","

        build(root)
        return self.res[:-1]

    def deserialize(self, data):
        if not data:
            return []
        a = data.split(",")
        q = collections.deque()
        for i in a:
            q.append(i)

        def build(q):
            if len(q) == 0:
                return None
            a = q.pop()
            if a == "#":
                return None
            root = TreeNode(a)
            root.right = build(q)
            root.left = build(q)
            return root

        return build(q)
