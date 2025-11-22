#array
def getFrequenzy(arr, st):
    freqarr = {}
    for x in arr:
        if x in freqarr:
            freqarr[x]+=1
        else:
            freqarr[x] = 1
#string
    freqstr = {}
    for c in st:
        freqstr[c] = freqstr.get(c , 0) + 1 
    return freqarr , freqstr 

arr = [4,1,4,2,1,4]
st = "banana"
print(getFrequenzy(arr , st))

#find count of max element
def mostFrequent(arr):
    freq = {}

    for x in arr:
        freq[x] = freq.get(x , 0) + 1

    freq_element = None
    freq_count  = 0 

    for element ,  count in freq.items():
        if count > freq_count:
            freq_count = count
            freq_element = element

    return freq_element , freq_count

arrary = [4,1,4,2,1,4]
print(mostFrequent(arrary))