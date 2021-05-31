def mergeLL(headOne, headTwo):
    p1 = headOne
    p2 = headTwo
    prev = None

    while p1 is not None and p2 is not None:
        if p1.value < p2.value:
            prev = p1
            p1 = p1.next
        else:
            if prev is not None:
                prev.next = p2
            prev = p2
            p2 = p2.next
            prev.next = p1

    if p1 is None:
        prev.next = p2

    return headOne if headOne.value < headTwo.value else headTwo