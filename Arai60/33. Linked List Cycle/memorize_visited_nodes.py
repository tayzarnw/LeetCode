# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        while head:
            visited_nodes.add(head)
            if head.next in visited_nodes:
                return True
            head = head.next

        return False
