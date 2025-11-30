# ---------------------------------------------------------
#  Find the Smallest Missing Positive Integer
#  (O(n) time, O(1) extra space) – Optimized Cyclic Placement
# ---------------------------------------------------------
#
#  PROBLEM:
#  Given an unsorted array of integers (which may include
#  negatives, zeros, and duplicates), return the smallest
#  positive integer (>= 1) that does *not* appear in the array.
#
#  Example:
#      Input:  [3, 4, -1, 1]
#      Output: 2
#
#  ---------------------------------------------------------
#  KEY IDEA (Index Mapping Trick):
#
#  For any value x in the range [1, n], its correct position
#  should be at index (x - 1).
#
#        value 1 → index 0
#        value 2 → index 1
#        value 3 → index 2
#        ...
#        value n → index (n - 1)
#
#  If we rearrange the array such that every valid number is
#  placed in its "home index", then the first index i where:
#
#        orderNumbers[i] != i + 1
#
#  directly gives us the missing positive integer (i + 1).
#
#  ---------------------------------------------------------
#  APPROACH:
#
#  STEP 1 — Cyclic Swapping (O(n)):
#      Use a pointer i and keep swapping values into their
#      correct positions *as long as*:
#          • number is in the range [1, n]
#          • and not already in its correct index
#
#      This ensures each number is moved at most once.
#
#  STEP 2 — Scanning for the first mismatch (O(n)):
#      After rearrangement:
#          If orderNumbers[i] != i + 1:
#              smallest missing = i + 1
#
#  STEP 3 — All numbers in correct place:
#      If array contains [1, 2, 3, ..., n]
#      then the missing number is (n + 1).
#
#  ---------------------------------------------------------
#  WHY THIS WORKS:
#
#  • Uses in-place cyclic placement.
#  • Avoids extra memory (constant space).
#  • Avoids sorting (O(n log n)).
#  • Guarantees linear time because each number is swapped
#    at most once into its “home index”.
#
#  ---------------------------------------------------------
#  TIME COMPLEXITY:
#        O(n)  → each element moved at most once
#
#  SPACE COMPLEXITY:
#        O(1)  → uses only a few pointers/variables
#
#  ---------------------------------------------------------
#  EDGE CASES:
#      • Empty array → return 1
#      • All negatives → return 1
#      • Missing number is at start, middle, or end
#      • Duplicate values handled safely
#      • Large range values ignored properly
#
# ---------------------------------------------------------
def findSmallestMissingPositive(orderNumbers):
    n = len(orderNumbers)
    i = 0
    while i < n:
        correct_index = orderNumbers[i]-1
        if 1<= orderNumbers[i] <= n and orderNumbers[i] != orderNumbers[correct_index]:
            orderNumbers[i] , orderNumbers[correct_index] = orderNumbers[correct_index] , orderNumbers[i]
        else:
            i+=1
    for i in range(n):
        if orderNumbers[i] != i+1:
            return i+1
    return n+1
