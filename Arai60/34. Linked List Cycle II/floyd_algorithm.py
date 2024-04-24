# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        cycle_exists = False

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                cycle_exists = True
                break

        if cycle_exists:
            slow = head
            while slow != fast:
                fast = fast.next
                slow = slow.next
            return slow

        return None
