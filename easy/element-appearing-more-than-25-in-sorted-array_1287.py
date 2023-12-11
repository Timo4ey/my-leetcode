# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

# Example 1:

# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6
# Example 2:

# Input: arr = [1,1]
# Output: 1


# Constraints:

# 1 <= arr.length <= 104
# 0 <= arr[i] <= 105

# ---------------------------------------Runtime 86 ms Beats 79.77% Memory 18.1 MB Beats 19.18%---------------------------------------

from collections import Counter
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c = Counter(arr)
        n = len(arr)
        return next(filter(lambda x: c[x] / n > 0.25, c))
