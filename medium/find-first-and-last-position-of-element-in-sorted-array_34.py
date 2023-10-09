# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

# ---------------------------------------Runtime 83 ms Beats 63.27% Memory 17.5 MB Beats 97.83%---------------------------------------

from typing import List

# Time complexity O(log n * m)


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []

        def binSearch():
            start, end = 0, len(nums) - 1
            while start <= end:
                middle = (start + end) // 2
                guess = nums[middle]
                if guess == target:
                    left = right = middle
                    while left - 1 >= 0 and nums[left - 1] == target:
                        left -= 1
                    while (
                        right + 1 <= len(nums) - 1
                        and nums[right + 1] == target
                    ):
                        right += 1

                    res.extend([left, right])

                    return res
                if guess > target:
                    end = middle - 1
                if guess < target:
                    start = middle + 1

        return binSearch() or [-1, -1]
