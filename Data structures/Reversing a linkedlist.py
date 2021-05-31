# iterative approach
# def reverseLL(head):
#     curr = head
#     prev = None
#
#     while curr is not None:
#         next = curr.next
#         curr.next = prev
#         prev = curr
#         curr = next
#     return prev

# recursive approach
def reverseLL(head):
    if not head or not head.next: return head
    p = reverseLL(head.next)
    head.next.next = head
    head.next = None
    return p