
    """
    Maximize the number of non-overlapping meetings using a classic greedy strategy.

    Problem:
        Given a list of meeting intervals [start, end], choose the maximum number
        of meetings such that no two selected meetings overlap.

    Approach:
        1. Sort all meetings by their end time (earliest finishing first).
        2. Select the first meeting after sorting.
        3. For every next meeting:
               - If its start time is >= the end time of the last selected meeting,
                 we can safely take it.
        4. Count how many non-overlapping meetings we select.

    Why Greedy Works:
        Choosing the meeting that ends earliest leaves maximum room for future
        meetings. This is the optimal strategy for interval scheduling.

    Time Complexity:
        O(n log n) due to sorting.

    Parameters:
        meetings (List[List[int]]): Array of [start, end] intervals.

    Returns:
        int: Maximum number of non-overlapping meetings.
    """
def maximizeNonOverlappingMeetings(meetings):
    if not meetings:
        return 0
    meetings.sort(key = lambda x:x[1])
    count = 1
    start = 0
    prev_end = meetings[0][1]
    for i in range(1,len(meetings)):
        start = meetings[i][0]
        if start >= prev_end:
            count += 1
            prev_end = meetings[i][1]
    return count
        
