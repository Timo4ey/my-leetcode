# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

# You must implement a solution with a linear runtime complexity and use only constant extra space.


# Example 1:

# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:

# Input: nums = [0,1,0,1,0,1,99]
# Output: 99

# ---------------------------------------Runtime 80 ms Beats 48.49% Memory 17.7 MB Beats 83.89%---------------------------------------

from collections import Counter
from typing import List


# Time Complexity O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return min(counter, key=counter.get)


# Solution @kshatriyas user XOR


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0

        for num in nums:
            ones ^= num & ~twos
            twos ^= num & ~ones

        return ones
