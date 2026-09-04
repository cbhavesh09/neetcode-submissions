# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        ocurr = head
        while ocurr:
            if ocurr.val==val:
                ocurr = ocurr.next 
            else:
                curr.next = ocurr
                curr = curr.next
                ocurr = ocurr.next
        curr.next = None
        return dummy.next