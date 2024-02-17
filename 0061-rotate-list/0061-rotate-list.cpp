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

// !!!!仅供复习观察用，以前写的解答的Python自动转的C++
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head) return nullptr;
        
        ListNode* lead = new ListNode(0);
        lead->next = head;
        ListNode* p = head;
        int length = 0;
        while (p) {
            length++;
            p = p->next;
        }
        k %= length;  // when length == 0
        if (k == 0) return head;
        
        p = head;
        ListNode* q = head;
        for (int i = 0; i < k; ++i) {
            q = q->next;
        }
        while (q->next) {
            p = p->next;
            q = q->next;
        }
        
        // p->next is the new head
        lead->next = p->next;
        p->next = nullptr;
        q->next = head;
        
        ListNode* newHead = lead->next;
        delete lead;
        return newHead;
    }
};
