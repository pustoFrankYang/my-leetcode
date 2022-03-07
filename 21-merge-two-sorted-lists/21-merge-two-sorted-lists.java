/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list2 == null) return list1;
        if (list1 == null) return list2;
        ListNode p = list1;
        ListNode q = list2;
        if (p.val > q.val) { // p always least
            p = list2;
            q = list1;
        }
        ListNode head = p; // head to return
        while (p.next != null && q != null) {
            if (q.val < p.next.val) {
                ListNode t = p.next;
                p.next = q;
                q = q.next;
                p = p.next;
                p.next = t;
            } else {
                p = p.next;
            }
        }
        if (q != null)
            p.next = q;
        return head;
    }
}