# Car Fleet 🚗💨

## Problem Statement

N cars are going to the same destination along a one-lane road. The destination is target miles away.

Each car i has a constant speed `speed[i]` (in miles per hour), and initial position `position[i]` miles towards the target along the road.

A car fleet is some non-empty set of cars driving at the same speed. Note that a single car is also a car fleet.

If a car catches up to another car while they are at the same position, the car will still be part of the same car fleet as it will just be following the other car.

Each car has a distinct, unique initial position.

Determine the total number of car fleets that will arrive at the destination.

## Approach 🛠️

I've used a stack-based approach to determine the total number of car fleets.

1. I created a list of pairs `[position[i], speed[i]]` for each car.
2. I sorted the list of pairs in reverse order based on the initial positions of the cars.
3. I initialized an empty stack to keep track of the time it takes for each car to reach the destination.
4. I iterated through the sorted list of pairs.
5. For each car, I calculated the time it would take to reach the destination using the formula `(target - position) / speed`.
6. If the stack is empty or the calculated time is greater than the time at the top of the stack, I pushed the calculated time onto the stack.
7. The final result was the length of the stack, which represents the total number of car fleets.

## Complexity Analysis ⚙️

- Time Complexity: O(n log n), where n is the number of cars.
  - The sorting step dominates the time complexity.
- Space Complexity: O(n), where n is the number of cars.
  - The space used by the stack is proportional to the number of cars.
