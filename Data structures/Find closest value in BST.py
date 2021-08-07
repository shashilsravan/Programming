def findClosestValue(tree, target, closest = float("inf")):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValue(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValue(tree.right, target, closest)
    else:
        return closest
