# Check Palindrome by Filtering Non-Letters
# ----------------------------------------
# This function determines whether a given string is a palindrome
# **when considering only alphabetic characters** and ignoring case.
#
# Steps used:
# 1. Filter out all non-alphabetic characters using str.isalpha().
# 2. Convert all remaining characters to lowercase (case-insensitive comparison).
# 3. Reverse the processed list and compare it with the original.
#
# Example:
#   Input:  "A1b2B!a"
#   After filtering → ['A','b','B','a']
#   After lowercasing → ['a','b','b','a']
#   Reverse → ['a','b','b','a']
#   Since they match, it is a palindrome → return 1
#
# Complexity:
# - Time:  O(n)  (one scan to filter, one to lowercase, one comparison)
# - Space: O(n)  (storing filtered characters)
#
# Returns:
# - 1 if the alphabetic-only string is a palindrome
# - 0 otherwise
def isAlphabeticPalindrome(code):
    # If empty string, treat as palindrome (per constraints)
    if not code:
        return 0

    # Step 1: Keep only alphabetic characters
    alphabets = list(filter(str.isalpha, code))

    # Step 2: Convert all letters to lowercase
    lowercase = [ch.lower() for ch in alphabets]

    # Step 3: Reverse and compare
    if lowercase == lowercase[::-1]:
        return 1
    return 0
