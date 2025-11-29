# ---------------------------------------------------------
#  Merge Overlapping Intervals (IBM / HackerRank Style)
# ---------------------------------------------------------
#
#  PROBLEM:
#  Given a list of intervals where each interval is represented
#  as [start, end], merge all overlapping intervals and return
#  a sorted list of non-overlapping intervals.
#
#  Example:
#      Input:  [[1,3], [2,6], [8,10], [15,18]]
#      Output: [[1,6], [8,10], [15,18]]
#
#  APPROACH:
#  1. If the list is empty, return empty.
#  2. Sort intervals by start time.
#  3. Initialize the merged list with the first interval.
#  4. For each remaining interval:
#         - Compare its start with the end of the last merged interval.
#         - If overlapping (start <= last_end):
#               Merge them by extending the end:
#               merged[-1][1] = max(last_end, current_end)
#         - Else:
#               They do not overlap → append interval as a new entry.
#
#  WHY SORT?
#      Ensures intervals are processed in increasing start order.
#      Without sorting, we cannot guarantee correct merging.
#
#  TIME COMPLEXITY:
#      O(n log n) due to sorting.
#      Merging itself is O(n).
#
#  SPACE COMPLEXITY:
#      O(n) for storing the merged list.
#
#  NOTES:
#      - Handles fully overlapping, partially overlapping,
#        and non-overlapping intervals.
#      - Works correctly for unsorted and duplicate intervals.
#      - Safe for edge cases such as n = 0 or n = 1.
#
# ---------------------------------------------------------
def mergeHighDefinitionIntervals(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x:x[0])
    
    merged = [intervals[0]]
    
    for start ,  end in intervals[1:]:
        last_start , last_end = merged[-1]
        
        if start <= last_end:
            merged[-1][1] = max(last_end , end)
        else:
            merged.append([start, end])
    
    return merged 
