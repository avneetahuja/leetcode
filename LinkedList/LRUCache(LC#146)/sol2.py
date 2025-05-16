class Node:
    def __init__(self, key, val):
        self.key,self.val,self.l,self.r = key, val, None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.r = self.tail
        self.tail.l = self.head
        
        self.capacity = capacity
    
    def insert_at_head(self,node):
        node.r = self.head.r
        self.head.r.l = node
        self.head.r = node
        node.l = self.head 
    def delete_from_tail(self):
        node = self.tail.l
        self.tail.l = self.tail.l.l
        self.tail.l.r = self.tail
        key = node.key
        return key


    def delete(self,key):
        node = self.head
        while node:
            if node.key == key:
                break
            node = node.r
        node.l.r = node.r
        node.r.l = node.l

        return node


    def get(self, key: int) -> int:
        if key in self.map:
            node = self.delete(key)
            self.insert_at_head(node)
            return self.map[key].val
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.map:                                    
            existing = self.delete(key)                        
            existing.val = value                               
            self.insert_at_head(existing)                      
            self.map[key] = existing                           
            return                                            


        if len(self.map) == self.capacity:
            old_key = self.delete_from_tail()
            del self.map[old_key]


        node = Node(key, value)
        self.insert_at_head(node)
        self.map[key] = node




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
