# ---------------------------------------------------------------
# Queue Implementation Using Two Stacks (Amortized O(1) Operations)
# 
# Problem:
# Implement a FIFO queue using two LIFO stacks such that
#   - enqueue(x)
#   - dequeue()
#   - peek()
#   - size()
# all run in amortized O(1) time.
#
# Technique:
# We maintain two stacks:
#   1. in_stack  → used during enqueue()
#   2. out_stack → used during dequeue() / peek()
#
# Key Idea:
# - enqueue(x) simply pushes x onto in_stack (O(1)).
# - For dequeues/peeks:
#       If out_stack is empty, we transfer ALL elements from in_stack to out_stack
#       by repeatedly popping from in_stack and pushing onto out_stack.
#
#       This reversal restores FIFO order:
#              front of queue = top of out_stack.
#
# - This transfer occurs only when needed — once per batch.
#   Therefore, each element is moved at most *once*, giving amortized O(1) time.
#
# Algorithm Summary:
#   enqueue(x):  push x onto in_stack
#   dequeue():   if out_stack empty → refill from in_stack, then pop from out_stack
#   peek():      same as dequeue, but return top instead of popping
#   size():      total = len(in_stack) + len(out_stack)
#
# Why Amortized O(1)?
# - Every element is pushed once into in_stack,
#   moved at most once into out_stack,
#   and popped once.
#   → Total O(n) operations for n enqueues/dequeues → O(1) amortized.
#
# Returns:
# An array collecting outputs of all non-enqueue operations
# in the order they occur (peek, dequeue, size).
# ---------------------------------------------------------------

def processRequestQueueOperations(operations, values):
    instack = []
    outstack = []
    result = []
    for op , v in zip(operations, values):
        if op == "enqueue":
            instack.append(v)
        elif op == "peek":
            if not outstack:
                while instack:
                    x = instack.pop()
                    outstack.append(x)
            result.append(outstack[-1])
        elif op == "dequeue":
            if not outstack:
                while instack:
                    x = instack.pop()
                    outstack.append(x)
            result.append(outstack.pop())
        elif op == "size":
            result.append(len(instack) + len(outstack))    
    return result  
