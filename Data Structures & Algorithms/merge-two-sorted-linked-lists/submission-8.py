# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        listf = ListNode(0)
        listfa = listf
        while curr1 and curr2:
            if curr1.val<curr2.val:
                listfa.next = curr1
                curr1 = curr1.next
            else:
                listfa.next = curr2
                curr2 = curr2.next
            listfa = listfa.next
        if curr1:
            listfa.next = curr1
        if curr2:
            listfa.next = curr2
        return listf.next
            

        