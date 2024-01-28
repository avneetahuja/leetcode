# LRU Cache Implementation 🧠

## Problem Statement

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: `get` and `put`.

`get(key)` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

`put(key, value)` - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.

Both the `get` and `put` operations should be done in constant time.

## Approach 🛠️

I've implemented an LRUCache using a doubly linked list and a hash map.

- The doubly linked list helps in maintaining the order of recently used items.
- The hash map helps in quickly checking whether a key exists in the cache and retrieving the corresponding node.

### Methods:

1. `insert(node: Node)`: Inserts a new node at the beginning of the doubly linked list.

2. `delete(node)`: Deletes a node from the doubly linked list.

3. `get(key: int) -> int`: Retrieves the value corresponding to the given key. If the key is found, the corresponding node is moved to the beginning of the list.

4. `put(key: int, value: int) -> None`: Inserts a new node with the given key and value. If the key already exists, the corresponding node is moved to the beginning. If the cache exceeds its capacity, the least recently used item is removed.

## Complexity Analysis ⚙️

- Time Complexity:
  - `get` and `put` operations: O(1)
  - Inserting and deleting nodes in the doubly linked list: O(1)
- Space Complexity: O(capacity) for storing nodes in the doubly linked list and O(capacity) for the hash map.
