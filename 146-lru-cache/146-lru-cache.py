# ¡¡¡¡gesah that should use linked list
class ListNode():
    def __init__(self, key=0, val=0, prev=None, nexter=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nexter
class LRUCache:

    def __init__(self, capacity: int):
        self.k2n = {}
        self.size = 0
        self.capacity = capacity
        # oldest will be tail.prev
        self.head, self.tail = ListNode(), ListNode()
        
        self.head.next, self.tail.prev = self.tail, self.head
        

    def get(self, key: int) -> int:
        curr = self.k2n.get(key, None)
        if curr:  # update existing
            curr.prev.next, curr.next.prev = curr.next, curr.prev
            self.head.next, curr.next = curr, self.head.next
            curr.next.prev = curr
            curr.prev = self.head
            
            return curr.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        curr = self.k2n.get(key, None)
        if curr:  # update existing
            curr.val = value
            curr.prev.next, curr.next.prev = curr.next, curr.prev
            self.head.next, curr.next = curr, self.head.next
            curr.next.prev = curr
            curr.prev = self.head
        else:  # add and delete
            if self.size >= self.capacity:
                self.k2n.pop(self.tail.prev.key)
                # !!!! order matters...
                self.tail.prev.prev.next, self.tail.prev = self.tail, self.tail.prev.prev
            else:
                self.size += 1
                
            curr = ListNode(key, value, self.head, self.head.next)
            self.head.next.prev, self.head.next = curr, curr
            self.k2n[key] = curr


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)