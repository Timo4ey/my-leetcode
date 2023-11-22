# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1


# ---------------------------------------Runtime 206 ms Beats 90.22% Memory 17.7 MB Beats 71.48%---------------------------------------

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            midl = (start + end) // 2
            guess = nums[midl]
            if guess == target:
                return midl
            elif guess < target:
                start = midl + 1
            elif guess > target:
                end = midl - 1
        return -1
