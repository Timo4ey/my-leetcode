# You are given an array of strings words and a string pref.

# Return the number of strings in words that contain pref as a prefix.

# A prefix of a string s is any leading contiguous substring of s.

# Example 1:

# Input: words = ["pay","attention","practice","attend"], pref = "at"
# Output: 2
# Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
# Example 2:

# Input: words = ["leetcode","win","loops","success"], pref = "code"
# Output: 0
# Explanation: There are no strings that contain "code" as a prefix.

# ---------------------------------------Runtime 44 ms Beats 80.28% Memory 16.3 MB Beats 85.52%---------------------------------------


from functools import reduce
from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return reduce(lambda acc, x: acc + int(x.find(pref) == 0), words, 0)
