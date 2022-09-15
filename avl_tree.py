class AVLNode(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.height = 1


class AVLTree(object):
    def insert(self, root, key):
        if root is None:
            return AVLNode(key)

        if key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and key < root.left.value:
            return self.rotate_right(root)

        if balance < -1 and key > root.right.value:
            return self.rotate_left(root)

        if balance > 1 and key > root.left.value:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and key < root.right.value:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def rotate_right(self, root):
        grandparent = root
        parent = grandparent.left
        child = parent.right

        parent.right = grandparent
        grandparent.left = child

        grandparent.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        parent.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        return parent

    def rotate_left(self, root):
        grandparent = root
        parent = grandparent.right
        child = parent.left

        parent.left = grandparent
        grandparent.right = child

        grandparent.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        parent.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        return parent

    def get_height(self, root):
        if root is None:
            return 0

        return root.height

    def get_balance(self, root):
        if root is None:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)

    def print_preorder(self, root):
        if root is None:
            return
        else:
            print(root.value)
            self.print_preorder(root.left)
            self.print_preorder(root.right)
