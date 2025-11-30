# --------------------------------------------------------------------
#  Count Number Pairs (Brute-Force O(n²) Approach)
# --------------------------------------------------------------------
#  PROBLEM:
#      Given a sorted array of positive integers and a target budget,
#      count the number of index pairs (i, j) such that:
#
#                     i < j  AND  prices[i] + prices[j] <= budget
#
#  EXAMPLE:
#      prices = [1, 2, 3, 4, 5], budget = 7
#      Valid pairs:
#         (1,2), (1,3), (1,4), (1,5),
#         (2,3), (2,4), (2,5), (3,4)
#      Output: 8
#
# --------------------------------------------------------------------
#  APPROACH (Brute Force):
#      • Use nested loops to consider every pair (i, j)
#      • Since the array is sorted, once prices[i] + prices[j] > budget,
#        all further j values will also be too large → break inner loop
#      • Valid pairs are counted one-by-one using count += 1
#
#  -------------------------------------------------------------------
#  TIME COMPLEXITY:
#      O(n²)
#      Acceptable because n ≤ 1000 (max 1,000,000 checks)
#
#  SPACE COMPLEXITY:
#      O(1) — no extra structures used
#
# --------------------------------------------------------------------
def countAffordablePairs(prices, budget):
    n = len(prices)
    if n < 2:
        return 0

    count = 0
    prices.sort()

    for i in range(n):
        for j in range(i + 1, n):
            if prices[i] + prices[j] <= budget:
                count += 1
            else:
                break  # sorted array → all further j only increase the sum

    return count
# --------------------------------------------------------------------
#  Count Number Pairs (Optimized Two-Pointer O(n) Approach)
# --------------------------------------------------------------------
#  KEY IDEA:
#      Since the array is sorted, we can use two pointers:
#
#          left = 0, right = n-1
#
#      • If prices[left] + prices[right] <= budget:
#            then ALL pairs (left, left+1), ..., (left, right) are valid
#            so we add (right - left) to count at once and move left++
#
#      • If prices[left] + prices[right] > budget:
#            move right-- to reduce the sum
#
#      This avoids checking every pair individually.
#
# --------------------------------------------------------------------
#  WHY count += (right - left)?
#      Example:
#          left=0 → value=1
#          right=3 → value=4
#          Sum = 5 <= budget
#
#      Valid pairs:
#          (1,4), (1,3), (1,2) → 3 pairs at once
#
# --------------------------------------------------------------------
#  TIME COMPLEXITY:
#      O(n)
#
#  SPACE COMPLEXITY:
#      O(1)
#
# --------------------------------------------------------------------
def countAffordablePairs_Optimized(prices, budget):
    n = len(prices)
    if n < 2:
        return 0

    prices.sort()
    left = 0
    right = n - 1
    count = 0

    while left < right:
        if prices[left] + prices[right] <= budget:
            # all pairs (left, left+1), ... , (left, right) are valid
            count += (right - left)
            left += 1
        else:
            right -= 1

    return count
