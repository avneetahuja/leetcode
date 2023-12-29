# Generate Parentheses ♺

## Problem Statement

Given `n` pairs of parentheses, generate all combinations of well-formed parentheses.

## Approach 🛠️

I've used a recursive approach to generate all combinations of well-formed parentheses.

1. I initialized an empty stack (`stack`) and an empty list (`ans`) to store the result.
2. I defined a recursive function (`generate`) that takes two parameters (`openCount` and `closeCount`) representing the counts of open and close parentheses.
3. In the recursive function:
   - If both `openCount` and `closeCount` are equal to `n`, I added the current combination to the result list (`ans`).
   - If `closeCount` is less than `openCount`, I added a closing parenthesis to the stack and made a recursive call to `generate` with updated `closeCount`.
   - If `openCount` is less than `n`, I added an opening parenthesis to the stack and made a recursive call to `generate` with updated `openCount`.
4. The function was called initially with `generate(0,0)` to start the recursive process.
5. The final result was the list of all combinations of well-formed parentheses.

## Complexity Analysis ⚙️

- Time Complexity: O(4^n / sqrt(n)), where n is the given number of pairs of parentheses.
  - The total number of combinations is the nth Catalan number, which is O(4^n / sqrt(n)).
- Space Complexity: O(4^n / sqrt(n)), where n is the given number of pairs of parentheses.
  - The space used by the recursive stack is proportional to the number of combinations.
