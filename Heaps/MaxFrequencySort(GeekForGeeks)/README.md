# Frequency Sort 📊

## Problem Statement

You are given an array `arr` of size `n`. Your task is to sort the array based on the frequency of elements in non-increasing order, i.e., the element with the highest frequency should appear first, followed by elements with decreasing frequencies.

## Approach 🚀

To sort the array based on the frequency of elements, we can use a min-heap to keep track of the frequency of each element. We'll iterate through the array to count the frequency of each element and store it in a dictionary. Then, we'll push each element-frequency pair into the min-heap. Finally, we'll pop elements from the heap and append them to the result list based on their frequencies.

### Steps:
1. Create an empty min-heap `heap` and an empty dictionary `map` to store the frequency of elements.
2. Iterate through the array `arr` and for each element, do the following:
   - Update the frequency of the element in the `map`.
3. Iterate through the key-value pairs in the `map` dictionary, and for each pair, do the following:
   - Push the pair `(frequency, element)` into the min-heap.
4. Iterate through the elements in the min-heap and for each element, do the following:
   - Append the element to the result list `li` based on its frequency (i.e., push the element `-frequency` times into `li`).
5. Return the result list `li`.

## Complexity Analysis ⚙️

- Time Complexity: O(N * log(N)), where N is the number of elements in the array `arr`.
  - Building the min-heap: O(N * log(N))
  - Extracting elements from the heap: O(N * log(N))
- Space Complexity: O(N)
  - We use additional space for the min-heap and the dictionary to store the frequency of elements.
