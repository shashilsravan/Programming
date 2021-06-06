def invertBinaryTree(tree):
    if tree is None:
        return
    swapChildren(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


def swapChildren(tree):
    tree.left, tree.right = tree.right, tree.left