# Number of Recent Calls

## Problem Description

The problem "Number of Recent Calls" from LeetCode requires us to implement a class `RecentCounter` that counts the number of recent requests within a sliding window of 3000 milliseconds (or 3 seconds). 

### Requirements

1. **Initialization**: The `RecentCounter` object needs to be initialized.
2. **ping(int t)**: Each call to this method represents a new request at time `t` (in milliseconds). The method should return the number of requests that have been made in the past 3000 milliseconds (including the new request).

## Solution

To solve this problem, we can use a double-ended queue (deque) which efficiently supports adding elements to the end and removing elements from the beginning. 

Here's a detailed explanation of the provided solution:

### Code

```python
from collections import deque

class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
```

### Explanation

1. **Initialization (`__init__` method)**:
    - A deque `self.q` is initialized to store the timestamps of the pings.

2. **Ping Method (`ping` method)**:
    - **Appending**: The current timestamp `t` is appended to the deque.
    - **Cleaning up old pings**: A while loop is used to remove all timestamps from the deque that are older than `t - 3000` milliseconds. This ensures that only the pings within the last 3000 milliseconds are kept.
    - **Counting**: The length of the deque is returned, representing the number of pings in the last 3000 milliseconds.

### Key Points

- **Efficiency**: Using a deque ensures that both the append and pop operations are performed in constant time, making the solution efficient.
- **Sliding Window**: By maintaining only the timestamps within the last 3000 milliseconds, we effectively implement a sliding window to count recent pings.
