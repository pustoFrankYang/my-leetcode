# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Q86m, 79.71%
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        llead = ListNode(0, None)
        llast = ListNode(0, None)
        glead = ListNode(0, None)
        glast = ListNode(0, None)
        p = head
        while p:
            if p.val < x:
                if llead.next is None:
                    llead.next = p
                else:
                    llast.next = p
                llast = p
            else:
                if glead.next is None:
                    glead.next = p
                else:
                    glast.next = p
                glast = p
            p = p.next
        llast.next = glead.next
        glast.next = None
        if llead.next is None:  # !!!caution
            llead.next = glead.next
        return llead.next