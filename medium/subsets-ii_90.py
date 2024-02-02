# Given an integer array nums that may contain duplicates, return all possible
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]


# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10

# ---------------------------------------Runtime 38 ms Beats 76.67% Memory 16.53 MB Beats 89.52%---------------------------------------

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = set()

        def backtracking(arr: List[int], path: List[int]) -> None:
            t = tuple(sorted(path))
            if t not in result:
                result.add(t)
            for i, v in enumerate(arr):
                path.append(v)
                backtracking(arr[i + 1:], path)
                path.pop()

        backtracking(nums, [])
        return result
