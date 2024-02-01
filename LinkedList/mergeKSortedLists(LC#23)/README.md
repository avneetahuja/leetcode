# Merge k Sorted Lists 🔄

## Problem Statement

Merge k sorted linked lists and return it as one sorted list.

## Approach 🛠️

The solution utilizes a divide-and-conquer approach to repeatedly merge pairs of linked lists until there is only one merged list remaining.

1. If the input list of linked lists is empty, return `None`.
2. While the length of the list of linked lists is greater than 1:
   - Create an empty list (`merged`) to store the merged pairs of linked lists.
   - Iterate through the list of linked lists in steps of 2.
   - For each pair of linked lists (list1 and list2), merge them using the `merge` function and append the result to the `merged` list.
   - Update the list of linked lists to be the `merged` list.
3. Return the final merged list.

The `merge` function takes two linked lists as input and merges them in sorted order:

1. If one of the linked lists is empty, return the other list.
2. Initialize a pointer (`head`) to the smaller of the first nodes of the two linked lists.
3. Iterate through the linked lists until one of them becomes empty:
   - Compare the current nodes of the two linked lists.
   - Connect the smaller node to the merged list (`curr`) and move to the next node in the respective linked list.
4. Connect the remaining nodes of the non-empty linked list to the merged list.
5. Return the merged list.

## Complexity Analysis ⚙️

- Time Complexity: O(N log k), where N is the total number of nodes across all linked lists, and k is the number of linked lists.
  - The solution iterates through each node once during the merging process.
  - The divide-and-conquer approach ensures logarithmic depth in the merging process.
- Space Complexity: O(1).
  - The solution uses a constant amount of extra space.
