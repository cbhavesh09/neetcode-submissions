# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse(curr):
            prev = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        curr = head
        prev = reverse(curr)
        p = None
        if n == 1:
            prev = prev.next
        else:
            p = prev 
            for x in range(n-2):
                p = p.next
            p.next = p.next.next
        ans = reverse(prev)
            
        return ans
    




        