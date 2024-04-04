# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(None)
        current = result
        carry = 0

        while l1 or l2 or carry > 0:
            if l1:
                left = l1.val
                l1 = l1.next
            else:
                left = 0
            if l2:
                right = l2.val
                l2 = l2.next
            else:
                right = 0

            carry += left + right
            digit = carry % 10
            carry //= 10
            current.next = ListNode(digit, None)
            current = current.next

        return result.next
