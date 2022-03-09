/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
    let lead = new ListNode(0, head);
    let p = lead; 
    let q = lead.next;
    while (q && q.next) {
        // when it reaches [p:a,q:b,c], q goes to c, no q.next, so break;
        // when it reaches [p:a,q:b,b], q go until no q.next, 
        //                            and p.next is set to null, break;
        if (p.next.val != q.next.val)
            p = p.next, q = p.next;
        else {
            while (q.next && q.val == q.next.val)
                q = q.next;
            p.next = q.next;
            q = p.next;
        }
        
    }
    return lead.next;
};