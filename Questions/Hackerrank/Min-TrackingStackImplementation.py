"""
Min-Tracking Stack (O(1) getMin) — Two Stack Approach
-----------------------------------------------------

This implementation supports:
    • push(x)
    • pop()
    • top()
    • getMin()
all in constant O(1) time.

Concept:
--------
We maintain TWO stacks:
1. stack     → stores all pushed values normally
2. min_stack → stores the minimum value at each level of the stack

Why it works:
-------------
Whenever we push a new value:
    - we also push the minimum between the new value and the previous minimum
      onto min_stack.
    - this means min_stack[i] always represents the minimum of stack[0..i]

Whenever we pop:
    - we pop from BOTH stacks, keeping them aligned

For top() → return the top of stack
For getMin() → return the top of min_stack (current minimum)

Example:
--------
Operations:
push 2 → min = 2
push 0 → min = 0
push 3 → min = 0
push 0 → min = 0
getMin → 0
pop    → remove top-level (0)
getMin → still 0

Time Complexity:
----------------
Each operation is O(1)
Space complexity O(n)

This approach is widely accepted in coding interviews (LeetCode, HackerRank,
IBM, Amazon, etc.).
"""

def processCouponStackOperations(operations):
    stack = []
    minstack = []
    result = []
    
    for op in operations:
        parts = op.split()
        if parts[0] == "push":
            x = int(parts[1])
            if not minstack:
                minstack.append(x)
            else:
                minstack.append(min(x, minstack[-1]))
            stack.append(x)
        elif parts[0] == "pop":
            stack.pop()
            minstack.pop()
        elif parts[0] == "top":
            result.append(stack[-1])
        elif parts[0] == "getMin":
            result.append(minstack[-1])
        
    return result    
