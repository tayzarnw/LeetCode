class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None

        dummy = ListNode(0, head)
        current = head
        previous = dummy

        while current and current.next:
            while current.next and current.val == current.next.val:
                current = current.next

            if previous.next != current:
                previous.next = current.next
            else:
                previous = previous.next

            current = current.next

        return dummy.next
