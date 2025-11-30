# --------------------------------------------------------------------
#  Binary Search — Find First Occurrence of Target in Sorted Array
# --------------------------------------------------------------------
#  PROBLEM:
#      Given a sorted array (may contain duplicates) and a target value,
#      return the index of the **first occurrence** of the target.
#      If the target is not found, return -1.
#
#  EXAMPLE:
#      nums   = [1, 2, 2, 2, 3]
#      target = 2
#      Output = 1   # first index where 2 appears
#
#  -------------------------------------------------------------------
#  APPROACH:
#      Use a modified binary search:
#
#          • Compute mid = (low + high) // 2
#          • If nums[mid] == target:
#                  - store mid in 'result'
#                  - search LEFT side to find earlier occurrences
#          • If nums[mid] < target:
#                  - search right half (low = mid + 1)
#          • Else:
#                  - search left half (high = mid - 1)
#
#      This ensures we find the FIRST index, not just any index.
#
#  -------------------------------------------------------------------
#  WHY WE MOVE 'high' WHEN WE FIND THE TARGET:
#      Even if nums[mid] == target, an earlier (lower index) copy may
#      exist. So we store the current mid, then shrink the search space
#      to the left half to find the first occurrence.
#
#  -------------------------------------------------------------------
#  TIME COMPLEXITY:
#      O(log n)     # binary search
#
#  SPACE COMPLEXITY:
#      O(1)         # only a few variables used
#
#  -------------------------------------------------------------------
#  EDGE CASES:
#      • Empty array → return -1
#      • No match → return -1
#      • All elements same → return index 0 if they equal target
#      • Multiple duplicates → return the first among them
#
# --------------------------------------------------------------------
def binarySearch(nums, target):
    if not nums:
        return -1

    low = 0
    high = len(nums) - 1
    result = -1  # store the first index where target is found

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            result = mid       # potential answer
            high = mid - 1     # keep searching left
        elif nums[mid] < target:
            low = mid + 1      # search right half
        else:
            high = mid - 1     # search left half

    return result
