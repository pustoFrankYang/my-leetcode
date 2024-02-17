#include <unordered_map>

// !!!仅供复习时观察用，原解答的python自动转到C++
class LRUCache {
private:
    struct ListNode {
        int key;
        int val;
        ListNode* prev;
        ListNode* next;
        ListNode(int k=0, int v=0, ListNode* p=nullptr, ListNode* n=nullptr) : key(k), val(v), prev(p), next(n) {}
    };
    
    int size;
    int capacity;
    ListNode* head;
    ListNode* tail;
    std::unordered_map<int, ListNode*> k2n;

public:
    LRUCache(int capacity) : size(0), capacity(capacity) {
        head = new ListNode();
        tail = new ListNode();
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) {
        if (k2n.find(key) != k2n.end()) {
            ListNode* curr = k2n[key];
            curr->prev->next = curr->next;
            curr->next->prev = curr->prev;
            moveToHead(curr);
            return curr->val;
        } else {
            return -1;
        }
    }
    
    void put(int key, int value) {
        if (k2n.find(key) != k2n.end()) {
            ListNode* curr = k2n[key];
            curr->val = value;
            curr->prev->next = curr->next;
            curr->next->prev = curr->prev;
            moveToHead(curr);
        } else {
            if (size >= capacity) {
                ListNode* last = tail->prev;
                k2n.erase(last->key);
                last->prev->next = tail;
                tail->prev = last->prev;
                delete last;
                size--;
            }
            ListNode* newNode = new ListNode(key, value, head, head->next);
            head->next->prev = newNode;
            head->next = newNode;
            k2n[key] = newNode;
            size++;
        }
    }
    
private:
    void moveToHead(ListNode* node) {
        node->prev = head;
        node->next = head->next;
        head->next->prev = node;
        head->next = node;
    }
};
