# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

# Return the kth positive integer that is missing from this array.


# Example 1:

# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
# Example 2:

# Input: arr = [1,2,3,4], k = 2
# Output: 6
# Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

# ---------------------------------------Runtime 59 ms Beats 42.73% Memory 16.6 MB Beats 5.59%---------------------------------------

from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        m = max(arr)
        s_arr = set(arr)
        c = 0

        for i in range(1, m**m + 1):
            if i not in s_arr:
                s_arr.add(i)
                c += 1
            if c == k:
                return i
        return arr[-1] + 1
