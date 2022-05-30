'''
序列化和反序列化树
使用前序遍历
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
            self.res = self.res + str(root.val) + ","
            build(root.left)
            build(root.right)

        build(root)
        return self.res

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
            a = q.popleft()
            if a == "#":
                return None
            root = TreeNode(a)
            root.left = build(q)
            root.right = build(q)
            return root

        return build(q)
