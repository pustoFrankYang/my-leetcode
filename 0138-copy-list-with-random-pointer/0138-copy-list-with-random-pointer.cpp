/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*, int> old2i;
        unordered_map<int, Node*> i2new;
        Node* lead = new Node(0);
        
        // copy except random
        Node *p = head, *q = lead;
        int ind = 0;
        while (p != NULL) {
            q->next = new Node(p->val);
            old2i[p] = ind;
            i2new[ind] = q->next;
            q = q->next;
            p = p->next;
            ind++; // !!!
        }
        
        // copy the random
        p = head, q = lead->next;
        while (p != NULL) {
            q->random = p->random == NULL? NULL : i2new[old2i[p->random]];
            p = p->next;
            q = q->next;
        }
        
        return lead->next;
    }
};