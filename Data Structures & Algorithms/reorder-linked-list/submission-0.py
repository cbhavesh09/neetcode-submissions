# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        prev = None
        while mid:
            nxt = mid.next
            mid.next = prev
            prev = mid
            mid = nxt
        new = head
        while prev:
            nxt1 = new.next
            new.next = prev
            nxt2 = prev.next
            prev.next = nxt1
            new = nxt1
            prev = nxt2


        