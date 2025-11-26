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