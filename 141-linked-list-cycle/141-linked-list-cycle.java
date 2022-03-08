/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
// 看解法用巧妙的快慢指针
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null) return false;
        if (head.next == head) return true;
        ListNode p, q;
        p = q = head;
        while (q != null) {
            if (q.next == p) return true;
            q = q.next;
            if (q == null) return false;
            else if (q.next == p) return true;
            q = q.next;
            p = p.next;
        }
        return false;
    }
}