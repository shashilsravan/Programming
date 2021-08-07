def isPalindrome(head) -> bool:
    if not head or not head.next:
        return True

    first = head
    second = head
    while second and second.next:
        first = first.next
        second = second.next.next

    prev = None
    while first:
        next = first.next
        first.next = prev
        prev = first
        first = next

    first = head
    second = prev
    while first and second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    return True