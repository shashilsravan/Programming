def removeNthNodeFromEnd(head, n):
    first = head
    second = head
    count = 1
    while count <= n:
        second = second.next
        count += 1
    # that means first is head node
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return

    # if it is not the first node
    while second is not None:
        second = second.next
        first = first.next

    # first is pointing to node right before the node we want to remove
    # so first.next = Node_To_Remove.next
    first.next = first.next.next
