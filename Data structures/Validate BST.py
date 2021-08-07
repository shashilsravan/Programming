def isValidBST(root):
    return BSTHelper(root, float("-inf"), float("inf"))


def BSTHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.val <= minValue or tree.val >= maxValue:
        return False
    leftIsValid = BSTHelper(tree.left, minValue, tree.val)
    return leftIsValid and BSTHelper(tree.right, tree.val, maxValue)