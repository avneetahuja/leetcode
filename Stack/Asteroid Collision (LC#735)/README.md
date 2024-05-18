# Asteroid Collision

## Problem Statement
You are given an array `asteroids` of integers representing asteroids in a row. For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed. Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

## Approach

### Steps

1. **Initialize a Stack**:
   - Use a stack to help simulate the collisions.
   
2. **Iterate Through Asteroids**:
   - For each asteroid in the input list:
     - If the stack is empty, append the asteroid to the stack.
     - If the asteroid is moving left (negative value):
       - Compare it with the top of the stack (which is moving right).
       - Handle collisions by comparing sizes and determine whether the top asteroid or the current asteroid (or both) should be removed.
       - Continue checking for collisions until no more collisions are possible.
     - If the asteroid is moving right (positive value), simply append it to the stack as it cannot collide with previous right-moving asteroids.

3. **Collision Handling**:
   - If the top of the stack asteroid is smaller, pop the stack and continue checking.
   - If both asteroids are of the same size, pop the stack and do not add the current asteroid.
   - If the current asteroid is smaller, do not add it to the stack.

### Solution Code

```python
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if not stack:
                stack.append(a)
            elif a < 0:
                flag = True
                while stack and stack[-1] > 0:
                    top = stack.pop()
                    if abs(a) > top:
                        continue
                    elif abs(a) == top:
                        flag = False
                        break
                    else:
                        flag = False
                        stack.append(top)
                        break
                if flag:
                    stack.append(a)
            else:
                stack.append(a)
        return stack
```

### Time Complexity
- The time complexity of this solution is O(n), where n is the number of asteroids. This is because each asteroid is processed once and each asteroid can be added and removed from the stack at most once.

### Space Complexity
- The space complexity is O(n) in the worst case, where no collisions occur, and all asteroids are stored in the stack.
