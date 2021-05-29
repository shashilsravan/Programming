class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        pass

    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        sol = ListNode()
        curr = sol
        carry = 0

        while l1 or l2 or carry:
            ans = 0
            if l1:
                ans += li.val
                li = li.next
            if l2:
                ans += l2.val
                l2 = l2.next
            if carry:
                ans += carry

            val = ans % 10
            carry = ans // 10
            curr.next = ListNode(val)
            curr = curr.next

        return sol.next

sol = Solution()
node11 = ListNode(2)
node12 = ListNode(4)

print(sol.addTwoNumbers(node11, node12).val)