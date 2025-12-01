"""
Next Greater Element with Distance (Brute Force)
------------------------------------------------

Problem:
    For each index i in the array 'readings', we want to find the next
    element to the RIGHT that is strictly greater than readings[i].
    
    If such an element exists at index j:
        - value    = readings[j]
        - distance = j - i  (the difference in positions)
        result[i]  = [value, distance]

    If no greater element exists to the right:
        result[i] = [-1, -1]

Approach (Beginner-Friendly, Brute Force):
    For each position i:
        - Look at every position j > i
        - The FIRST element that is greater becomes the answer
        - Stop immediately after finding it
        - If none is found, store [-1, -1]

Why this works:
    We check every element to the right until we find the first greater one.
    This directly matches the definition of "next greater element".

Time Complexity:
    O(n^2) in the worst case because of the nested loops.
    This approach is simple to understand and works well for smaller inputs.

Space Complexity:
    O(n) for storing the result.

This is a clear and easy method suitable for beginners.
"""
def findNextGreaterElementsWithDistance(readings):
    n = len(readings)
    result = []

    for i in range(n):
        value = readings[i]
        found = False

        for j in range(i + 1, n):
            if readings[j] > value:
                # value = readings[j]
                # distance = j - i  (NOT j - 1)
                result.append([readings[j], j - i])
                found = True
                break

        if not found:
            result.append([-1, -1])

    return result
