# Sliding Window – Maximum Sum Subarray of Size K
# This algorithm finds the maximum sum of any subarray of length K in O(n) time.
# Steps:
# Compute sum of first K elements
# Slide the window by removing the outgoing element and adding the incoming one
# Track the maximum sum seen so far
# Return the maximum sum
# This is an important and common pattern for IBM and HackerRank coding tests.
def maxSumWindow(arr, K):
    sum = 0
    maxsum = 0
    
    # Step 1: calculate initial window sum
    for i in range(K):
        sum += arr[i]
    maxsum = sum
    
    # Step 2: slide the window
    for i in range(K, len(arr)):
        sum = sum - arr[i-K] + arr[i]
        if sum > maxsum:
            maxsum = sum
    
    return maxsum

# ---------------------------------------------------------
#  Count Unique Substrings of Size K  (Sliding Window - Easy)
# ---------------------------------------------------------
#
#  PROBLEM:
#  Given a string s and an integer K, count how many substrings
#  of length K contain ALL unique (non-repeating) characters.
#
# ---------------------------------------------------------
#  SLIDING WINDOW CONCEPT:
#  We slide a fixed-size window of length K across the string.
#  For each window:
#       - Extract substring s[i : i+K]
#       - Convert to a set (duplicates removed)
#       - If size of set == K → all characters are unique → count++
#
# ---------------------------------------------------------
#  WHY range(len(s) - K + 1)?
#
#  A window of size K starting at index i is:
#       window = s[i : i+K]
#
#  This window is valid only if:
#       i + K - 1 <= len(s) - 1
#  →     i <= len(s) - K
#
#  So valid start positions are 0 to (len(s) - K).
#  Total valid windows = len(s) - K + 1
#
#  Example:
#       s = "abcabcabc" (length 9)
#       K = 3
#       Valid windows = 9 - 3 + 1 = 7
#
#       Windows:
#       s[0:3] = "abc"
#       s[1:4] = "bca"
#       s[2:5] = "cab"
#       s[3:6] = "abc"
#       s[4:7] = "bca"
#       s[5:8] = "cab"
#       s[6:9] = "abc"
#
# ---------------------------------------------------------
#  TIME COMPLEXITY:
#       O(n * K)   (set(window) for each window)
#
#  SPACE COMPLEXITY:
#       O(K)
#
# ---------------------------------------------------------
#  CODE:

def countUniqueSubstrings(s, K):
    count = 0
    for i in range(len(s) - K + 1):
        window = s[i:i+K]
        if len(set(window)) == K:
            count += 1
    return count

s = "abcabc"
K = 3
print(countUniqueSubstrings(s, K))

# ---------------------------------------------------------
#  Longest Substring Without Repeating Characters
#  Sliding Window (Easy Version)
# ---------------------------------------------------------
#
#  PROBLEM:
#  Given a string s, find the length of the longest substring
#  that contains NO repeating characters.
#
# ---------------------------------------------------------
#  APPROACH: SLIDING WINDOW + SET
#
#  We use two pointers (left and right) to represent a window.
#  As the right pointer expands the window:
#       - If the character is NOT in the set → add it
#       - If the character IS in the set → shrink window
#
#  A set (char_set) is used to store characters in the current window.
#
# ---------------------------------------------------------
#  WHY "WHILE" AND NOT "IF"?
#
#  If a repeating character is found, we must shrink the window
#  UNTIL that character is removed.
#
#  Example: "aabc"
#    window = "aa" → shrink once → "a"
#    still duplicate → shrink again → ""
#
#  This requires multiple removals → so we use WHILE.
#
# ---------------------------------------------------------
#  LOGIC:
#
#  left = 0
#  for each right pointer:
#
#       while s[right] already in window:
#           remove s[left] from set
#           left += 1
#
#       add s[right] to set
#       update max_len = max(max_len, window_size)
#
#  Window size = right - left + 1
#
# ---------------------------------------------------------
#  TIME COMPLEXITY:
#       O(n)      (each char added & removed at most once)
#
#  SPACE COMPLEXITY:
#       O(min(n, charset))     (set of characters)
#
# ---------------------------------------------------------
#  CODE:
def longestUniqueSubstring(s):
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len

s = "pwwkew"
print(longestUniqueSubstring(s))
