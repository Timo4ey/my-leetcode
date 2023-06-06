
# A string is good if there are no repeated characters.

# Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

# A substring is a contiguous sequence of characters in a string.

# Example 1:

# Input: s = "xyzzaz"
# Output: 1
# Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
# The only good substring of length 3 is "xyz".
# Example 2:

# Input: s = "aababcabc"
# Output: 4
# Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
# The good substrings are "abc", "bca", "cab", and "abc".


# ---------------------------------------Runtime 44 ms Beats 59.82% Memory 16.4 MB Beats 13.67%---------------------------------------

# My solution
# Time complexity O(n)
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k: int = 3
        res: int = 0
        for i in range(len(s) - k + 1):
            if len(set(s[i:i + k])) >= k:
                res += 1
        return res
