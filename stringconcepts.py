#1 Count
def getCount(stri):
    count_v = 0
    count_c = 0
    count_d = 0 
    count_s = 0
    for ch in stri:
        if ch.lower() in "aeiou":
            count_v += 1
        elif ch.isalpha():
            count_c += 1
        elif ch.isdigit():
            count_d += 1 
        else:
            count_s += 1
        
    return count_v , count_c , count_d , count_s

stri = "Hello123@"
count_v , count_c , count_d , count_s  = getCount(stri)
print(f"Vowels = {count_v} \n Consonants = {count_c} \n Digits = {count_d} \n Special Characters = {count_s}")

# Check if a String Has All Unique Characters
def isUniqueString(s):
    seen = set()

    for ch in s:
        if ch not in seen:
            seen.add(ch)
        else:
            return  f" False because '{ch}' repeats"
    return True

s = "abcde"
print(isUniqueString(s))

#Palindrome
def isPalindrome(s):
    rev = ""
    for i in range(len(s)-1,-1,-1):
        rev += s[i]

    return s == rev
        

print(isPalindrome("madam"))
#easy way
def isPalindrome(s):
    return s == s[::-1]

print(isPalindrome("madam"))

#stringreversal
def stringReversal(s):
    rev = ""
    for i in range(len(s)-1 , -1, -1):
        rev += s[i]
    #can use s[::-1] to reverse
    return rev

s = "Python"
print(stringReversal(s))

#Remove Duplicates from a String
def removeDuplicates(s):
    seen = set()
    result = ""
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result += ch
        else:
            continue
    return result

s = "mississippi"
print(removeDuplicates(s))

#Find the First Non-Repeating Character in a String
def firstUnique(s):
    count_dict = {}
    for ch in s:
        count_dict[ch] = count_dict.get(ch,0) + 1
    
    for ch in s:
        if count_dict[ch] == 1:
            return ch
    return None
    
s = "mississippi"
print(firstUnique(s))

#Anagrams
def areAnagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    
    count1 = {}
    count2 = {}
    for ch in s1:
        count1[ch] = count1.get(ch , 0) + 1
    for ch in s2:
        count2[ch] = count2.get(ch , 0) + 1
    return count1 == count2

s1 = "hello"
s2 = "bello"
print(areAnagrams(s1 , s2))