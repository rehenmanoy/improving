#Subarray Sum Exists (Brute Force Method) Pattern 1
# Loop through all possible start positions i
# For each i, loop through all end positions j ≥ i
# Keep a running sum of elements between i and j
# If at any point the sum equals K, return True
# If all subarrays are checked and none match, return False
def subarraySumExists(arr, K):
    n = len(arr)
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]
            if sum == K:
                return True
    return False

arr = [1, 2, 3, 7, 5]
K = 13
print(subarraySumExists(arr, K))

#Count Subarrays With Sum = K
def countSubarraysWithSum(arr, K):
    count = 0
    n = len(arr)
    for i in range(n):
        current_sum = 0
        for j in range(i,n):
            current_sum+=arr[j]
            if current_sum == K:
                count += 1
    return count

arr = [1, 2, 1, 2, 1]
K = 3
print(countSubarraysWithSum(arr,K))

#Maximum Subarray Sum (Kadane’s Algorithm) 
# ✔ Step 1: Initialize
# current_sum = 0
# max_sum = -∞ (to handle cases where all numbers are negative)
# ✔ Step 2: Loop through each element x
# Add the number to current_sum
# Update max_sum if current_sum is now the largest
# If current_sum becomes negative, reset it to 0
# (because a negative start only hurts future sums)
# ✔ Step 3: Return max_sum
def maxSubarraySum(arr):
    max_sum = float('-inf')
    current_sum = 0

    for x in arr:
        current_sum += x
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    
    return max_sum

arr = [-2, 3, -1, 2, -3]
print(maxSubarraySum(arr))
