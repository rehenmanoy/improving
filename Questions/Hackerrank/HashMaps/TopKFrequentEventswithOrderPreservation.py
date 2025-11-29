# ---------------------------------------------------------
#  Top K Frequent Events (with Order Preservation)
#  IBM / HackerRank Style Problem
# ---------------------------------------------------------
#
#  PROBLEM:
#  Given a list of event IDs and an integer k, return the k most
#  frequent events. If two events have the same frequency, the one
#  that appears earlier in the original list must come first.
#
#  EXAMPLES:
#      Input:  events = [1,2,1,3,2,1],  k = 2
#      Output: [1, 2]
#
#      Input:  events = [4,4,1,2,2,3,1,3,2],  k = 3
#      Output: [2, 4, 1]
#
#  ---------------------------------------------------------
#  APPROACH:
#
#  1. Frequency Count
#       Use a dictionary to count occurrences of each event.
#         example:
#             frequenzy = { 1:3, 2:2, 3:1 }
#
#  2. Track First Occurrence
#       For tie-breaking, store the index at which each distinct
#       event first appears.
#         example:
#             first_index = { 1:0, 2:1, 3:3 }
#
#  3. Build Sortable Tuple List
#       For each event ID, create a tuple:
#
#            (-frequency, first_index, value)
#
#       Why?
#         • Negative frequency → sorts in descending order
#         • Smaller first_index → earlier appearance wins ties
#         • Value → event ID carried at the end
#
#  4. Sort the tuple list
#       Python sorts tuples lexicographically:
#            1. by -frequency
#            2. by first_index
#            3. by event value (not required, but harmless)
#
#  5. Extract Top K Values
#       After sorting, take first k items and extract the event IDs.
#
#  ---------------------------------------------------------
#  TIME COMPLEXITY:
#      • Counting frequencies:   O(n)
#      • Tracking first index:   O(n)
#      • Sorting distinct events: O(D log D)
#           where D = number of distinct elements
#      Total: O(n + D log D)
#
#  SPACE COMPLEXITY:
#      O(D) for frequency + first_index + sortable list
#
#  ---------------------------------------------------------
#  EDGE CASES:
#      • k = 0 → return []
#      • events = [] → return []
#      • All values identical → return first k occurrences
#
# ---------------------------------------------------------
def getTopKFrequentEvents(events, k):
    if k == 0 or not events:
        return []
    
    frequenzy = {}
    for x in events:
        frequenzy[x] = frequenzy.get(x , 0) + 1
    first_index = {}
    for i , x in enumerate(events):
        if x not in first_index:
            first_index[x] = i
    
    sortable = []
    for value in frequenzy:
        sortable.append((-frequenzy[value], first_index[value] , value))
    
    sortable.sort()
    
    result = [value for (_,_,value) in sortable[:k]]
    return result
