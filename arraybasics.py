#Second Largest Distinct Element
def secondLargest(arr):
    unique = list(set(arr)) #get unique items from array
    if len(unique) < 2:
        return None
    unique.sort()
    return unique[-2]

arr = [1,4,2,4,3]
print(secondLargest(arr))

#Smallest difference between any two elements
def smallestDiff(arr):
    arr.sort()
    min_diff = float('inf')
    for x in range(1, len(arr)):
        diff = arr[x] - arr[x-1]
        min_diff = min(min_diff , diff)
    
    return min_diff

arr = [4,9,1,32,13]
print(smallestDiff(arr))

#Two-Sum Using Set
def twoSum(arr , target):
    seen = set()

    for x in arr:
        if target - x in seen:
            return True
        else:
            seen.add(x)
    
    return False

arr = [2,7,11,15]
target = 9
print(twoSum(arr , target))