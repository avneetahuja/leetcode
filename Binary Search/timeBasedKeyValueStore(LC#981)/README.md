# Time-Based Key-Value Store ⌛🔑

## Problem Statement

Design a time-based key-value data structure that can perform two operations:

1. `set(string key, string value, int timestamp)`: Stores the key-value pair `(key, value)` with the given timestamp.
2. `get(string key, int timestamp)`: Returns a value such that `set(key, value, timestamp_prev)` was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns an empty string (`""`).

## Approach 🛠️

I've implemented a solution using a binary search approach. The key-value pairs for each key are stored in a list, sorted by timestamps. The `get` operation uses binary search to find the largest timestamp less than or equal to the given timestamp.

## Class Definition

### TimeMap

#### Properties
- `map`: A dictionary to store the key-value pairs with timestamps.

#### Methods
- `__init__(self)`: Initializes an empty TimeMap.
- `set(self, key: str, value: str, timestamp: int) -> None`: Stores the key-value pair `(key, value)` with the given timestamp.
- `get(self, key: str, timestamp: int) -> str`: Returns a value associated with the largest timestamp less than or equal to the given timestamp.

## Complexity Analysis ⚙️

- Time Complexity: 
  - `set` operation: O(1)
  - `get` operation: O(log n), where n is the number of timestamps for a given key.
- Space Complexity: O(n), where n is the total number of key-value pairs.
