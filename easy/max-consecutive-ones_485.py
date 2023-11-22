# Given a binary array nums, return the maximum number of consecutive 1's in the array.


# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:


# Input: nums = [1,0,1,1,0,1]
# Output: 2
# ---------------------------------------Runtime 344 ms Beats 59.20% Memory 16.5 MB Beats 18.45%---------------------------------------

from typing import List


# My solution
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cons, count = float("-inf"), 0
        for i in nums:
            if i:
                count += i
            if not i:
                max_cons, count = (
                    (count, 0) if max_cons < count else (max_cons, 0)
                )
        return max_cons if max_cons > count else count
