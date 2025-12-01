"""
Custom Fibonacci Sequence (IBM Coding Round – Medium)

Problem:
--------
Compute the n-th number in a modified Fibonacci sequence where indexing is 0-based
and the first two values are defined as:
    F(0) = 1
    F(1) = 2

Every other value follows the recurrence:
    F(n) = F(n - 1) + F(n - 2)

Examples:
---------
Input: n = 3
Sequence: [1, 2, 3, 5]
Output: 5

Input: n = 10
Sequence: [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
Output: 144

Approach:
---------
- This is a simple dynamic programming / iterative Fibonacci generation.
- Since n ≤ 92, values fit in 64-bit integers.
- We precompute Fibonacci values up to index 92 using a list and return fibo[n].
- Time Complexity:  O(n)
- Space Complexity: O(n)

Notes:
------
- Memoization or bottom-up DP both work; this implementation uses iterative DP.
- The function safely handles input n = 0 or n = 1 using predefined starting values.

"""
def getAutoSaveInterval(n):
    if n < 0:      # invalid input guard
        return 0

    fibo = [1, 2]  # base values: F(0) = 1, F(1) = 2

    # Precompute up to max needed (92)
    for i in range(2, 100):
        fibo.append(fibo[i - 1] + fibo[i - 2])

    return fibo[n]
