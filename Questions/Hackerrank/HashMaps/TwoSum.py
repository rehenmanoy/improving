# ---------------------------------------------------------
#  Two Sum – Find Task Pair for Given Slot Length
#  (IBM / HackerRank Style Problem)
# ---------------------------------------------------------
#
#  PROBLEM:
#  You are given a list of task durations and a target slot length.
#  The goal is to find two distinct indices (i, j) such that:
#
#        taskDurations[i] + taskDurations[j] = slotLength
#
#  If multiple pairs exist, any one valid pair may be returned.
#  If no pair exists, return [-1, -1].
#
# ---------------------------------------------------------
#  APPROACH (Optimal O(n) Solution Using Hash Map):
#
#  • We loop through the array once.
#  • For each element `duration`, compute the value we still need:
#
#        needed = slotLength - duration
#
#  • If `needed` already exists in the dictionary, we found a pair.
#    The dictionary stores the index where that earlier value appeared.
#
#        return [seen[needed], current_index]
#
#  • If not found, store the current duration with its index:
#
#        seen[duration] = current_index
#
#  • If the loop ends with no valid pair, return [-1, -1].
#
# ---------------------------------------------------------
#  WHY HASH MAP?
#
#  • Instant lookup of the needed value in O(1) time.
#  • Avoids nested loops and reduces time complexity from:
#
#        O(n²)  →  O(n)
#
# ---------------------------------------------------------
#  CONSTRAINTS:
#
#  • 0 <= n <= 1000
#  • 1 <= taskDurations[i] <= 1,000,000
#  • 1 <= slotLength <= 2,000,000
#  • Return indices, not the values
#
# ---------------------------------------------------------
#  TIME COMPLEXITY:
#      O(n) – single pass through the list
#
#  SPACE COMPLEXITY:
#      O(n) – hashmap storing values and their indices
#
# ---------------------------------------------------------
#  EXAMPLE:
#      Input:
#         taskDurations = [2, 7, 11, 15]
#         slotLength = 9
#
#      Output:
#         [0, 1]  (because 2 + 7 = 9)
#
# ---------------------------------------------------------
def findTaskPairForSlot(taskDurations, slotLength):
    seen = {}
    
    for i in range(len(taskDurations)):
        needed = slotLength - taskDurations[i]
        if needed in seen:
            return [seen[needed], i]
        seen[taskDurations[i]] = i             
            
    return [-1,-1]  
