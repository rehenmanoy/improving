"""
Compute Peak Concurrent Sessions per Group
------------------------------------------

This function processes a list of login/logout events and calculates, 
for each group, the maximum number of users who were logged in at the 
same time ("peak concurrency").

Each event is a list of four strings:
    [timestamp, user_id, group_id, event_type]
Where:
    - timestamp  : string representing an integer time
    - user_id    : string (not used for aggregation)
    - group_id   : string representing group identifier
    - event_type : "login" or "logout"

Key Points:
-----------
1. Events may be UNSORTED, so we sort them by:
       (timestamp, login/logout priority)
   We always process "login" BEFORE "logout" at the same timestamp
   so that a login-logout at the same time counts as 1 active session.

2. For each group, we simulate the timeline:
       - On "login":  current_active[group] += 1
                      update peak if needed
       - On "logout": current_active[group] -= 1

3. We track:
       current[group_id] : number of currently logged-in users
       peak[group_id]    : maximum concurrent sessions seen so far

4. The final result is returned as a sorted list of:
       [group_id, peak_concurrent_sessions]

Time Complexity:
    O(N log N) due to sorting N events.
Space Complexity:
    O(G) where G = number of distinct groups.

This simulation-based approach matches real-world processing of server logs,
authentication systems, and concurrency tracking — very common in IBM-style questions.
"""
def computeGroupPeakConcurrency(events):
    if not events:
        return []

    def sort_key(e):
        timestamp = int(e[0])
        activity = e[3]
        order= 0 if activity == "login" else 1
        return timestamp , order

    events.sort(key = sort_key)

    current = {}
    peak = {}

    for time, emp_id, grp_id_str , activity in events:
        grp_id = int(grp_id_str)
        if grp_id not in current:
            current[grp_id] = 0
            peak[grp_id] = 0
        if activity == "login":
            current[grp_id] += 1
            if current[grp_id] > peak[grp_id]:
                peak[grp_id] = current[grp_id]
        else:
            current[grp_id] -= 1
    
    result = []
    for grp_id , sesions in peak.items():
        result.append([grp_id , sesions])
    result.sort(key = lambda x:x[0])
    return result
