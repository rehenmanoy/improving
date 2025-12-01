"""
Zero-Sum Triplets within Sliding Window (Brute Force Version)
-------------------------------------------------------------

Problem:
    Given an integer array 'readings' and a 'windowSize', find all unique
    triplets (i, j, k) such that:

        1. i < j < k
        2. readings[i] + readings[j] + readings[k] == 0
        3. The triplet fits inside a sliding window:
               k - i + 1 <= windowSize
        4. Triplets must be unique (no duplicate value combinations).

Approach (Brute Force):
    For each starting index i:
        - Compute the maximum allowed index k (i + windowSize - 1).
        - Loop through all j (i+1 to max_k - 1).
        - Loop through all k (j+1 to max_k).
        - If the three values sum to zero, we sort the triplet and add it
          to a set to avoid duplicates.

Why sorting each triplet?
    Different index combinations may produce the same value set.
    Sorting ensures that:
        [1, -2, 1], [-2, 1, 1], [1, 1, -2]
    all become the same tuple: (-2, 1, 1)

Why store in a set?
    A set automatically removes duplicates, so we only keep unique triplets.

Complexity:
    Time Complexity: O(n * windowSize^2)
    Space Complexity: O(U) where U is the number of unique triplets.

Notes:
    - This brute-force solution is easy to understand and implement.
    - It may fail on very large inputs due to its nested loops, but is
      useful for learning sliding window constraints with triplets.
"""
def findZeroSumTripletsInWindow(readings, windowSize):
    n = len(readings)
    result_set = set()
    if windowSize < 3 or n < 3:
        return []
    
    for i in range(n):
        max_k = min(n-1, i+windowSize - 1)
        for j in range(i+1 , max_k):
            for k in range(j+1 , max_k+1):
                if readings[i]+readings[j]+readings[k] == 0:
                    trip = [readings[i], readings[j], readings[k]]
                    trip.sort()
                    result_set.add(tuple(trip))
    result = [list(t) for t in result_set]
    return result
