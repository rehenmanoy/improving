def getUniqueCount(arr):
    arr.sort()
    used = set()

    for x in arr:
        if x-1 > 0 and (x-1) not in used:
            used.add( x-1)
        elif x not in used:
            used.add(x)
        elif x+1 not in used:
            used.add(x+1)
    
    return len(used)


n = int(input("Enter Size Of Array:"))
arr = []
print("Enter Array Elements")
for _ in range(n):
    x = int(input())
    arr.append(x)
print(getUniqueCount(arr))