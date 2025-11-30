# Check for Non-Identical String Rotation
# ---------------------------------------
# The goal is to determine whether s2 is a **non-trivial rotation** of s1.
# A rotation means shifting characters circularly, such as:
#     "abcde" → "cdeab"  (rotate left by 2)
#
# REQUIREMENTS:
# - s2 must be a rotation of s1
# - s2 must NOT be identical to s1 (non-trivial rotation)
# - lengths must match
#
# APPROACH:
# 1. If lengths differ, return 0 immediately.
# 2. Convert both strings to lowercase (though constraints already guarantee lowercase).
# 3. Try all possible rotations of s1:
#       rotated = s1[d:] + s1[:d]
#    For each rotation:
#       - if rotated == s2 AND rotated != s1 → valid non-trivial rotation.
# 4. If no rotation matches, return 0.
#
# COMPLEXITY:
# - Time:  O(n²)  because each of n rotations creates a substring of size n.
# - Space: O(n)   due to rotated string creation.
#
# This is acceptable for n ≤ 1000 (max ~1 million character ops).
def isNonTrivialRotation(s1, s2):
    # Basic validation
    if len(s1) != len(s2):
        return 0

    # Normalize to lowercase
    s1_lower = s1.lower()
    s2_lower = s2.lower()

    # Try all rotations of s1
    for d in range(len(s1_lower)):
        rotated = s1_lower[d:] + s1_lower[:d]

        # Check non-trivial rotation
        if rotated != s1_lower and rotated == s2_lower:
            return 1

    return 0
