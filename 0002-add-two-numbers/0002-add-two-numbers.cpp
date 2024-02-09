/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        bool adds_one = false;
        ListNode* ans = new ListNode(0, NULL);
        ListNode* p = l1, *q = l2, *curr = ans;
        while (p != NULL && q != NULL) {
            int val = p->val + q->val;
            if (adds_one) { 
                val++;
                adds_one = false;
            }
            if (val >= 10) {
                val -= 10;
                adds_one = true;
            }
            curr->next = new ListNode(val, NULL);
            curr = curr->next;
            p = p->next;
            q = q->next;
        }
        
        if (p != NULL) {
            curr->next = p;
        }
        if (q != NULL) {
            curr->next = q;
        }
        while (adds_one) {
            if (curr->next == NULL) {
                curr->next = new ListNode(1, NULL);
                adds_one = false;
            } else {
                int val = curr->next->val + 1;
                adds_one = false;
                if (val >= 10) {
                    val -= 10;
                    adds_one = true;
                }
                curr->next->val = val;
                curr = curr->next;
            }
        }
        
        return ans->next;
    }
};