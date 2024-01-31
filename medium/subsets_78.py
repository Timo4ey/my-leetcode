# Given an integer array nums of unique elements, return all possible
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

# ---------------------------------------Runtime 36 ms Beats 75.54% Memory 16.79 MB Beats 60.34%---------------------------------------

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracing(arr: List[int], path: List[int]):
            result.append(path[:])

            for i in range(len(arr)):
                path.append(arr[i])
                backtracing(arr[i + 1 :], path)
                path.pop()

        backtracing(nums, [])
        return result
