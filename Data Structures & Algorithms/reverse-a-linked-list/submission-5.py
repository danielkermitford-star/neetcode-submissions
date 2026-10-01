# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        node = head
        prev = None
        while node.next:
            next = node.next
            node.next = prev
            prev = node
            node = next
        node.next = prev
        head = node
        return head
        