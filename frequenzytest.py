def getCountDictionary(str):
    count_dict = {}

    for ch in str:
        count_dict[ch] = count_dict.get(ch , 0) + 1
    
    return count_dict

str = "mississippi"
count_dict = getCountDictionary(str)
for key,values in count_dict.items():
    print(f"{key} : {values}")