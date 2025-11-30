# ---------------------------------------------------------
#  Count Elements Greater Than Previous Average
#  --------------------------------------------------------
#  PROBLEM:
#  Given an array of positive integers, return the number of
#  elements that are strictly greater than the average of all
#  previous elements. The first element is skipped since it
#  has no previous values.
#
#  Example:
#      Input:  [100, 200, 150, 300]
#      Output: 2
#
#      Day 1: 200 > avg(100)        → count = 1
#      Day 2: 150 > avg(100,200)?   → no
#      Day 3: 300 > avg(100,200,150)=150 → count = 2
#
# ----------------------------------------------------------
#  APPROACH:
#
#  • Maintain a running list (avg_arr) of all previous values.
#  • For each element at index i:
#        - compute average of all elements before i
#        - check if current value is strictly greater
#        - if yes → increment count
#        - add current value to avg_arr for future averages
#
#  This follows the problem exactly and is efficient enough
#  for n ≤ 1000 (constraints provided).
#
# ----------------------------------------------------------
#  TIME COMPLEXITY:
#      O(n²) because sum() is O(n) and runs for each element.
#      Acceptable for small n ≤ 1000.
#
#  SPACE COMPLEXITY:
#      O(n) for storing previous values.
#
# ----------------------------------------------------------
#  EDGE CASES:
#      • Empty list → return 0
#      • Single element → return 0
#
# ----------------------------------------------------------
def countResponseTimeRegressions(responseTimes):
    if not responseTimes:
        return 0
    n = len(responseTimes)
    avg_arr = [responseTimes[0]]
    count = 0
    for i in range(1,n):
        avg = sum(avg_arr) / len(avg_arr)
        if responseTimes[i] > avg:
            count+=1
        avg_arr.append(responseTimes[i])
    return count

#O(n) complexity one
def countResponseTimeRegressions(responseTimes):
    if not responseTimes:
        return 0
    
    prev_sum = responseTimes[0]
    count = 0
    
    for i in range(1, len(responseTimes)):
        avg = prev_sum / i
        if responseTimes[i] > avg:
            count += 1
        
        prev_sum += responseTimes[i]   # update running sum
    
    return count
