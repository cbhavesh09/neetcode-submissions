# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = prev = dummy
        if not slow.next:
            dummy.next = None
        while n:
            fast = fast.next
            n-=1
        while fast:
            prev = slow
            fast = fast.next
            slow = slow.next
        prev.next = slow.next
        return dummy.next
        

        