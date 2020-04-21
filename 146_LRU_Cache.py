class Node:    
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None

class LRUCache:
    # deque + hashmap # cannot use deque, need to use double linked list
    # get idea of using head and tail from Discuss channel -- brilliant
    # use _remove and _add logic help the cleaness of the code

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key in self.dic:
            n = self.dic[key]
            self._remove(self.dic[key])
            self._add(n)
            return n.v
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            n = self.dic[key]
            self._remove(self.dic[key])
            n.v = value
            self._add(n)
        else:            
            if len(self.dic.keys()) >= self.cap:
                del self.dic[self.head.next.k]
                self._remove(self.head.next)
            self.dic[key] = value
            node = Node(key, value)
            self._add(node)
            self.dic[key] = node
                            
    
    def _remove(self, node):
        n = node.next
        p = node.prev
        p.next = n
        n.prev = p
        
    
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)