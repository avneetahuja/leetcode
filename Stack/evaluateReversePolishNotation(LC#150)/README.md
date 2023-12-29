# Evaluate Reverse Polish Notation ⏮️🇵🇱🧮

## Problem Statement

Evaluate the value of an arithmetic expression in Reverse Polish Notation (RPN).

Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression.

Note:
- Division between two integers should truncate toward zero.
- The given RPN expression is always valid.

## Approach 🛠️

I've used a stack-based approach to evaluate the given Reverse Polish Notation expression.

1. I initialized an empty stack to store the operands.
2. I iterated through each token in the expression.
3. If the token is an operand (not an operator), I pushed it onto the stack.
4. If the token is an operator (`+`, `-`, `*`, `/`), I popped the required number of operands from the stack and performed the corresponding operation.
5. The result was then pushed back onto the stack.
6. The loop continued until all tokens were processed.
7. The final result was the only element left on the stack.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the number of tokens in the expression.
  - Each token is processed once.
- Space Complexity: O(n), where n is the number of tokens in the expression.
  - The space used by the stack is proportional to the number of operands.
