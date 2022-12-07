import avl_tree as avl
if __name__ == '__main__':
    tree = avl.AVLTree()
    root = None
    root = tree.insert(root, 25)
    root = tree.insert(root, 15)
    root = tree.insert(root, 50)
    root = tree.insert(root, 40)
    root = tree.insert(root, 35)
    root = tree.insert(root, 80)
    root = tree.insert(root, 10)
    root = tree.insert(root, 5)
    root = tree.insert(root, 45)

    tree.print_preorder(root)
