class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        self.connectTwo(root.left, root.right)

    def connectTwo(self, node1, node2):
        if not node1 or not node2:
            return
        node1.next = node2
        self.connectTwo(node1.left, node1.right)
        self.connectTwo(node2.left, node2.right)
        self.connectTwo(node1.right, node2.left)
