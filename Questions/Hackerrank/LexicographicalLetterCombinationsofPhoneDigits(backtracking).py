# --------------------------------------------------------------------
#  Lexicographical Letter Combinations of Phone Digits
# --------------------------------------------------------------------
#  PROBLEM:
#      We are given a string 'digits' made up of the characters '0'-'9'.
#      Each digit maps to some characters like on an old phone keypad:
#
#          '2' -> "abc"
#          '3' -> "def"
#          '4' -> "ghi"
#          '5' -> "jkl"
#          '6' -> "mno"
#          '7' -> "pqrs"
#          '8' -> "tuv"
#          '9' -> "wxyz"
#
#      For this problem, '0' and '1' map to themselves:
#
#          '0' -> "0"
#          '1' -> "1"
#
#      We must generate ALL possible strings that can be formed by:
#          - taking exactly ONE character from the mapping of each digit
#          - in the same order as the digits in the input
#
#      The result should be a list of all such combinations in
#      lexicographical (sorted) order.
#
#  EXAMPLES:
#  -------------------------------------------------------------------
#   1) digits = "23"
#
#      '2' -> "abc"
#      '3' -> "def"
#
#      Possible combinations:
#         a + d = "ad"
#         a + e = "ae"
#         a + f = "af"
#         b + d = "bd"
#         b + e = "be"
#         b + f = "bf"
#         c + d = "cd"
#         c + e = "ce"
#         c + f = "cf"
#
#      Final result:
#         ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
#   2) digits = "203"
#
#      '2' -> "abc"
#      '0' -> "0"
#      '3' -> "def"
#
#      So we pick one char from each:
#        - from "a/b/c"
#        - then "0"
#        - then "d/e/f"
#
#      Combinations:
#        "a0d", "a0e", "a0f",
#        "b0d", "b0e", "b0f",
#        "c0d", "c0e", "c0f"
#
#  -------------------------------------------------------------------
#  APPROACH: BACKTRACKING (RECURSION)
#  -------------------------------------------------------------------
#      This is a classic "build all combinations" problem.
#
#      At each position (index) in the 'digits' string, we have multiple
#      choices (every letter corresponding to that digit). We want to
#      explore ALL possible choices across ALL positions.
#
#      This can be visualized as a tree:
#
#          Example digits = "203"
#
#              index=0  ('2': a, b, c)
#              /    |     \
#            "a"   "b"    "c"
#              |     |      |
#          index=1  ('0': only "0")
#              |     |      |
#            "a0"  "b0"   "c0"
#              |     |      |
#          index=2  ('3': d, e, f)
#            /|\    /|\    /|\
#         "a0d"... etc ...
#
#      We use a recursive function:
#
#          backtrack(index, path)
#
#      where:
#          - index = current position in the 'digits' string
#          - path  = partial string built so far
#
#      BASE CASE:
#          If index == len(digits), it means we've chosen one character
#          for every digit, so 'path' is a complete combination.
#          We append it to the result list and RETURN (stop going deeper).
#
#      RECURSIVE CASE:
#          1. Look at the current digit: digit = digits[index]
#          2. Get its mapped characters: letters = mapping[digit]
#          3. For each character 'ch' in letters:
#                 - append 'ch' to the current path
#                 - move to the next index
#                 - this is: backtrack(index + 1, path + ch)
#
#      Because we:
#          - process digits from left to right,
#          - and for each digit process its letters in sorted order
#            ("abc", then "def", etc.),
#
#      the combinations are naturally generated in lexicographical order.
#      We can still call result.sort() at the end as a safety step.
#
#  -------------------------------------------------------------------
#  STEP-BY-STEP TRACE FOR digits = "203"
#  -------------------------------------------------------------------
#      mapping:
#          "2" -> "abc"
#          "0" -> "0"
#          "3" -> "def"
#
#      Call: backtrack(0, "")
#
#      index = 0, digit = '2', letters = "abc"
#
#      1) pick 'a':
#          backtrack(1, "a")
#
#          index = 1, digit = '0', letters = "0"
#          - pick '0':
#                backtrack(2, "a0")
#
#                index = 2, digit = '3', letters = "def"
#
#                • pick 'd':
#                       backtrack(3, "a0d")
#                       index == len(digits) == 3 -> save "a0d", return
#
#                • pick 'e':
#                       backtrack(3, "a0e")
#                       save "a0e", return
#
#                • pick 'f':
#                       backtrack(3, "a0f")
#                       save "a0f", return
#
#      2) go back, pick 'b' for the first digit:
#          backtrack(1, "b")
#          -> generates "b0d", "b0e", "b0f"
#
#      3) go back, pick 'c' for the first digit:
#          backtrack(1, "c")
#          -> generates "c0d", "c0e", "c0f"
#
#      Final 'result':
#          ["a0d","a0e","a0f","b0d","b0e","b0f","c0d","c0e","c0f"]
#
#  -------------------------------------------------------------------
#  WHY DO WE NEED "return" IN THE BASE CASE?
#  -------------------------------------------------------------------
#      In the base case:
#
#          if index == len(digits):
#              result.append(path)
#              return
#
#      we have finished building one full combination (path).
#      There are no more digits to process. If we do NOT return here,
#      the function will continue and try to access digits[index]
#      with index == len(digits), which would cause an IndexError.
#
#      The 'return' also tells recursion:
#          "Stop going deeper on this path; go back and try another
#           letter choice from the previous step."
#
#  -------------------------------------------------------------------
#  TIME COMPLEXITY:
#      Let N = len(digits), and each digit maps to up to 4 letters
#      (digit '7' and '9' have 4 letters).
#
#      In the worst case, total combinations = product of mapping sizes.
#      This can be up to at most 10^6 as per the problem constraint.
#
#      Time complexity is O(total_combinations * N) approximately,
#      since each combination is of length N and we build each once.
#
#  SPACE COMPLEXITY:
#      • O(total_combinations * N) to store all combinations in 'result'.
#      • O(N) recursion stack depth (one frame per digit).
#
# --------------------------------------------------------------------
def letterCombinations(digits):
    if not digits:
        return []

    mapping = {
        "0": "0",
        "1": "1",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    result = []

    def backtrack(index, path):
        # Base case: if we've processed all digits, save the combination
        if index == len(digits):
            result.append(path)
            return

        digit = digits[index]
        letters = mapping[digit]

        # Try each possible letter for this digit
        for ch in letters:
            backtrack(index + 1, path + ch)

    # Start from index 0 with an empty path
    backtrack(0, "")

    # Combinations are already generated in lexicographical order
    # due to the mapping strings being sorted, but sort for safety.
    result.sort()
    return result
