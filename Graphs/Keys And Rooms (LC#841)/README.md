# Can Visit All Rooms

## Problem Description

You are given an array `rooms` where `rooms[i]` is a list of keys in room `i`. Each key `rooms[i][j]` is an integer representing a key to a different room. Initially, you are in room 0, and you need to use the keys to access other rooms in the building. Return `true` if you can visit all the rooms, otherwise return `false`.

## Examples

### Example 1
- **Input**: `rooms = [[1],[2],[3],[]]`
- **Output**: `true`
- **Explanation**: We start in room 0 and pick up the key to room 1. In room 1, we pick up the key to room 2, and so on. We can visit all rooms.

### Example 2
- **Input**: `rooms = [[1,3],[3,0,1],[2],[0]]`
- **Output**: `false`
- **Explanation**: We cannot enter room 2 since the only key available is in room 2 itself.

## Approach

1. **Initialization**:
    - Initialize a `visited` list to track visited rooms.
    - Use a `to_visit` stack to manage rooms to visit next.

2. **DFS Implementation**:
    - Define a helper function `visit` that marks a room as visited and adds its keys to the `to_visit` stack.
    - Recursively visit rooms using the `to_visit` stack until it's empty.

3. **Check Completion**:
    - After attempting to visit all rooms, check if all rooms have been visited by examining the `visited` list.

## Solution Code

```python
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        to_visit = []
        
        def visit(i):
            if visited[i]:
                return
            visited[i] = True
            for room in rooms[i]:
                if not visited[room]:
                    to_visit.append(room)
            while len(to_visit) > 0:
                visit(to_visit.pop())
        
        visit(0)
        
        for room in visited:
            if not room:
                return False
        return True
```

## Explanation

1. **Initialization**:
    - `n` is the number of rooms.
    - `visited` is initialized to a list of `False` values, indicating that no rooms have been visited yet.
    - `to_visit` is an empty list that will be used as a stack for the DFS traversal.

2. **DFS Function (`visit`)**:
    - If the current room `i` has already been visited, return immediately.
    - Mark the current room `i` as visited.
    - Iterate through all keys in room `i` and add unvisited rooms to the `to_visit` stack.
    - Recursively visit rooms in the `to_visit` stack until it's empty.

3. **Completion Check**:
    - After visiting as many rooms as possible starting from room 0, iterate through the `visited` list.
    - If any room is found that hasn't been visited, return `False`.
    - If all rooms are visited, return `True`.

## Complexity Analysis

- **Time Complexity**: O(N + E), where N is the number of rooms and E is the total number of keys.
- **Space Complexity**: O(N) for the `visited` list and the recursion stack.
