# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        dummy = ListNode(0, head)
        current = head
        previous = dummy
        val_to_delete = -101

        while current.next:
            if current.val == current.next.val:
                val_to_delete = current.val

            if val_to_delete == current.val:
                previous.next = current.next
            else:
                previous = previous.next

            current = current.next

        if val_to_delete == current.val:
            previous.next = current.next

        return dummy.next
