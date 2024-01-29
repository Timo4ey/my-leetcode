# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


# Constraints:

# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10

# ---------------------------------------Runtime 127 ms Beats 23.88% Memory 17.00 MB Beats 62.03%---------------------------------------

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        seen = set()

        def swap(arr: list, n: int) -> None:
            if n < 2:
                seen.add(tuple(arr[:]))
            else:
                for j in range(n - 1, -1, -1):
                    arr[j], arr[n - 1] = arr[n - 1], arr[j]
                    swap(arr, n - 1)
                    arr[j], arr[n - 1] = arr[n - 1], arr[j]

        swap(nums, len(nums))
        return seen
