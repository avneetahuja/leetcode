# Min Stack ⬇️📚

## Problem Statement

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

- `push(val)` - Pushes the element `val` onto the stack.
- `pop()` - Removes the element on the top of the stack.
- `top()` - Retrieves the element on the top of the stack.
- `getMin()` - Retrieves the minimum element in the stack.

## Approach 🛠️

I've implemented the Min Stack using two stacks, `stack` and `minStack`.

1. I initialized two empty lists, `stack` and `minStack`.
2. The `stack` list is used to store the elements pushed onto the stack.
3. The `minStack` list is used to store the minimum element at each step.
4. When pushing an element, I compared it with the current minimum element (`val2`) in the `minStack`.
5. I pushed the element onto both `stack` and `minStack`, ensuring that `minStack` always reflects the minimum element at each step.
6. When popping an element, I removed the top elements from both `stack` and `minStack`.
7. The `top()` method returns the element at the top of `stack`.
8. The `getMin()` method returns the element at the top of `minStack`.

## Complexity Analysis ⚙️

- Time Complexity: O(1) for each operation.
  - All operations (push, pop, top, and getMin) are performed in constant time.
- Space Complexity: O(n), where n is the number of elements in the stack.
  - The space used is proportional to the number of elements stored in the stack.
