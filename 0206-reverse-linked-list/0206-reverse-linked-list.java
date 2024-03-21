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
    public ListNode reverseList(ListNode head) {
        ListNode lead = new ListNode();
        ListNode p = head;
        while (p != null) {
            ListNode temp = p;
            p = p.next;
            temp.next = lead.next;
            lead.next = temp;
        }
        return lead.next;
    }
}