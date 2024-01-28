class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next,self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.map={}
        self.size=0
        self.capacity = capacity
        self.head,self.tail = Node(0,0), Node(0,0)
        self.head.next = self.tail
        self.tail.prev=self.head
    
    def insert(self, node: Node):
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node
    
    def delete(self,node):
        nxt,prv = node.next,node.prev
        prv.next,nxt.prev = nxt, prv
        # self.map.pop(node.key)

    def get(self, key: int) -> int:
        if key in self.map:
            self.delete(self.map[key])
            self.insert(self.map[key])
            return self.map[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        newNode = Node(key,value)
        if key in self.map:
            self.delete(self.map[key])
            self.size-=1
        self.insert(newNode)
        self.size+=1
        self.map[key]=newNode
        if len(self.map)>self.capacity:
            lru = self.tail.prev
            self.delete(self.tail.prev)
            del self.map[lru.key]
    
    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
