# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lead = ListNode(0, head)
        p = q = lead
        for i in range(n + 1): # so p is pre
            q = q.next
        while q != None:
            p = p.next
            q = q.next
        p.next = p.next.next
        return lead.next