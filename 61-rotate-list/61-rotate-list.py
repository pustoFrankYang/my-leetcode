# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
RE
[]
0

[1]
0
'''
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return
        lead = ListNode(0, head)
        p = head
        lth = 0
        while p is not None:
            lth += 1
            p = p.next
        k %= lth  #### when length == 0
        if k == 0:  ####
            return head
        p, q = head, head
        for i in range(k):
            q = q.next
        while q.next is not None:
            p = p.next
            q = q.next
        # p,next is the new head
        lead.next = p.next
        p.next = None
        q.next = head
        return lead.next