# You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:

# pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
# Note that ^ denotes the bitwise-xor operation.

# It can be proven that the answer is unique.

# Example 1:

# Input: pref = [5,2,0,3,1]
# Output: [5,7,2,3,2]
# Explanation: From the array [5,7,2,3,2] we have the following:
# - pref[0] = 5.
# - pref[1] = 5 ^ 7 = 2.
# - pref[2] = 5 ^ 7 ^ 2 = 0.
# - pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
# - pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.
# Example 2:

# Input: pref = [13]
# Output: [13]
# Explanation: We have pref[0] = arr[0] = 13.
# ---------------------------------------Runtime 675 ms Beats 36.61% Memory 31.3 MB Beats 96.56%---------------------------------------

from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        i = len(pref) - 1
        while i > 0:
            pref[i] = pref[i] ^ pref[i - 1]
            i -= 1
        return pref
