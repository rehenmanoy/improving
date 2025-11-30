# --------------------------------------------------------------------
#  Find First Occurrence of Target in a Sorted Array (Binary Search)
# --------------------------------------------------------------------
#  PROBLEM:
#      Given a sorted array (may contain duplicates), return the index
#      of the FIRST occurrence of a target value. If the target is not
#      present, return -1.
#
#  EXAMPLE:
#      nums   = [1, 2, 2, 2, 3]
#      target = 2
#      Output = 1    # first index where 2 appears
#
#  --------------------------------------------------------------------
#  APPROACH (Binary Search):
#      Use a modified binary search that continues searching LEFT
#      even after finding the target.
#
#      • Compute mid = (low + high) // 2
#      • If nums[mid] == target:
#            - store mid in 'result'
#            - shrink search space: high = mid - 1
#            (because earlier occurrences may exist)
#
#      • If nums[mid] < target:
#            - search right: low = mid + 1
#
#      • If nums[mid] > target:
#            - search left: high = mid - 1
#
#      After loop ends, 'result' holds the FIRST occurrence.
#
#  --------------------------------------------------------------------
#  EDGE CASES:
#      • Empty array → return -1
#      • Target smaller than all elements → return -1
#      • Target greater than all elements → return -1
#      • Multiple duplicates → must return earliest index
#      • Single-element array → works normally
#
#  --------------------------------------------------------------------
#  TIME COMPLEXITY:   O(log n)
#  SPACE COMPLEXITY:  O(1)
#
# --------------------------------------------------------------------
def findFirstOccurrence(nums, target):
    if not nums:
        return -1

    low = 0
    high = len(nums) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            result = mid
            high = mid - 1    # keep searching left for earlier position
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result
