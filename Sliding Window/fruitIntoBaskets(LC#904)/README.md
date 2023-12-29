# Fruit Into Baskets 🍑🧺

## Problem Statement

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array `fruits` where `fruits[i]` is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

- You only have two baskets, and each basket can only hold a single type of fruit. 
- There is no limit on the amount of fruit each basket can hold.
- Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
- Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
- Given the integer array `fruits`, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

## Approach 🛠️

I've used a sliding window approach to find the total number of fruits that can be collected.

1. I initialized pointers `i` and `j` to define a sliding window.
2. I used a while loop to iterate through the list of fruits.
3. In each iteration:
   - I updated the count of each type of fruit in the current window (`fCount` dictionary).
   - If the number of unique fruits in the window is less than or equal to 2, I updated the maximum count (`mx`).
   - If the number of unique fruits exceeded 2, I adjusted the window by incrementing `i` until it became valid again.
4. The final result was the maximum count of fruits that can be collected.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the input list `fruits`.
  - The algorithm iterates through the list using a sliding window approach.
- Space Complexity: O(min(n, m)), where n is the length of the input list `fruits` and m is the size of the fruit type set (number of distinct fruit types).
  - The space used by the `fCount` dictionary is proportional to the size of the fruit type set.

Feel free to customize this README further based on additional details you want to provide or any specific formatting preferences you have.
