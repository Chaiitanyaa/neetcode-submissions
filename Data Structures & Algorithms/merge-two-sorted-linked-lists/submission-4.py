# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        
        node = ListNode()
        dummy = node

        
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        while curr1 != None and curr2 != None:
            if curr1.val >= curr2.val:
                node.next = curr2
                curr2 = curr2.next
                node = node.next
            else: 
                node.next = curr1
                curr1 = curr1.next
                node = node.next
        if curr1 is None:
            node.next = curr2
        else:
            node.next = curr1
        return dummy.next
