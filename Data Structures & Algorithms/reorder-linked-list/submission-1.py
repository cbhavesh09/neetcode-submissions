# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse_linkedlist(curr):
            prev = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next 
        slow.next= None
        rsecond = reverse_linkedlist(second)
        first = head
        while rsecond:
            nxt = first.next
            nxt2 = rsecond.next
            first.next = rsecond
            rsecond.next = nxt
            first = nxt
            rsecond = nxt2  


            
        