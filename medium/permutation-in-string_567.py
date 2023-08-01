# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.


# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
# ---------------------------------------Runtime 60 ms Beats 99.24% Memory 16.4 MB Beats 60.57%---------------------------------------


from collections import defaultdict


# Time Complexity O(n)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def isEqual(n1, n2):
            return n1 == n2

        sub = defaultdict(int)
        s1Dict = defaultdict(int)
        for string in s1:
            s1Dict[string] += 1

        k = len(s1)
        for string in s2[:k]:
            sub[string] += 1

        if isEqual(sub, s1Dict):
            return True
        prev = 0
        for indx in range(k, len(s2)):
            sub[s2[indx]] += 1
            if sub[s2[prev]] - 1 <= 0:
                del sub[s2[prev]]
            else:
                sub[s2[prev]] -= 1
            prev = indx - k + 1
            if isEqual(sub, s1Dict):
                return True

        return False
