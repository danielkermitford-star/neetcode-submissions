# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
    
        if list1.val < list2.val:  
            list1_2 = ListNode(list1.val)
            list1 = list1.next
        else:
            list1_2 = ListNode(list2.val)
            list2 = list2.next
        list1_2_it = list1_2
        while list1 and list2:
            if list1.val < list2.val:
                list1_2_it.next = ListNode(list1.val)
                list1 = list1.next
            else:
                list1_2_it.next = ListNode(list2.val)
                list2 = list2.next
            list1_2_it = list1_2_it.next
        if list1:
            list1_2_it.next = list1
        else:
            list1_2_it.next = list2
        return list1_2
        