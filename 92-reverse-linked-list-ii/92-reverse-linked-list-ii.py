# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Q92m, 87.22%
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lead = ListNode(0, head)
        start, end = lead, lead
        for i in range(1, right + 1):
            if i < left:
                start = start.next
            end = end.next
        tail = end.next
        vor = start
        start = start.next
        vor.next = tail
        for i in range(right - left + 1):
            p = start
            start = start.next
            p.next = vor.next
            vor.next = p
        return lead.next