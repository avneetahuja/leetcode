# Predict Party Victory

## Problem Description

In the Senate, there are `N` senators. Each senator can be either from the Radiant party ('R') or the Dire party ('D'). The senate has a procedure to determine the victorious party:
1. Each senator can vote to ban one senator of the opposite party.
2. If a senator is banned, they cannot participate in any further voting.
3. The voting continues in rounds until only one party has members remaining.

Given a string `senate` representing the order of senators and their parties, determine which party will be victorious.

## Example
- **Input:** `"RD"`
- **Output:** `"Radiant"`

- **Input:** `"RDD"`
- **Output:** `"Dire"`

## Approach

### Steps

1. **Count Initial Senators**:
   - Count the number of Radiant (`R`) and Dire (`D`) senators initially.

2. **Use a Queue for Voting Rounds**:
   - Use a queue to simulate the rounds of voting. Each senator is dequeued, votes, and if they are not banned, they are enqueued again.

3. **Banning Mechanism**:
   - Keep track of how many senators of each party are currently banned.
   - When a senator from one party votes, they can ban a senator from the opposite party if there are any unbanned senators left.
   - Adjust counts of senators and banned senators accordingly.

4. **Determine the Victorious Party**:
   - The process continues until one party has no senators left. The remaining party is declared the winner.

### Solution Code

```python
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rCount = dCount = 0
        for senator in senate:
            if senator == 'R':
                rCount += 1
            else:
                dCount += 1
        
        rCurrentBanned = dCurrentBanned = 0
        q = deque(senate)
        
        while not (rCount == 0 or dCount == 0):
            current = q.popleft()
            if current == 'R':
                if rCurrentBanned > 0:
                    rCurrentBanned -= 1
                    rCount -= 1
                else:
                    dCurrentBanned += 1
                    q.append(current)
            else:
                if dCurrentBanned > 0:
                    dCurrentBanned -= 1
                    dCount -= 1
                else:
                    rCurrentBanned += 1
                    q.append(current)
        
        return 'Radiant' if dCount == 0 else 'Dire'
```

### Explanation

1. **Count Initial Senators**:
   - Iterate through the `senate` string and count the number of 'R' and 'D' senators.

2. **Queue for Voting Rounds**:
   - Initialize a queue with the senators.

3. **Voting Process**:
   - Dequeue each senator and process their vote:
     - If a Radiant senator is dequeued and no Radiant senators are currently banned, they ban a Dire senator.
     - If a Dire senator is dequeued and no Dire senators are currently banned, they ban a Radiant senator.
     - If a senator is banned, they are not re-enqueued.

4. **Check for Victory**:
   - Continue this process until one party has no remaining senators.

5. **Return the Winner**:
   - Return 'Radiant' if there are no Dire senators left, otherwise return 'Dire'.

### Time Complexity
- The time complexity is O(n), where n is the length of the `senate` string. Each senator may be processed multiple times, but the operations per senator are constant time.

### Space Complexity
- The space complexity is O(n) due to the use of the queue to store the senators.
