class BinaryNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

    def add(self, val):
        if val <= self.value:
            if self.left:
                self.left.add(val)
            else:
                self.left = BinaryNode(val)
        else:
            if self.right:
                self.right.add(val)
            else:
                self.right = BinaryNode(val)

    def compute_height(self):
        height = -1
        if self.left:
            height = max(height, self.left.height)
        if self.right:
            height = max(height, self.right.height)

        self.height = height + 1


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = BinaryNode(val)
        else:
            self.root.add(val)

    def __contains__(self, item):
        node = self.root

        while node:
            if item < node.value:
                node = node.left
            elif item > node.value:
                node = node.right
            else:
                return True
        return False

    @property
    def height(self):
        if self.root:
            return self.root.height
        else:
            return -1
