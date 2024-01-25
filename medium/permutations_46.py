# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]


# Constraints:

# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.


# ---------------------------------------Runtime 38 ms Beats 85.22% Memory 16.90 MB Beats 56.39%---------------------------------------


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        N = len(nums)
        p = list(range(N + 1))
        i = 0

        while i < N:
            p[i] -= 1

            j = i % 2 * p[i]

            nums[i], nums[j] = nums[j], nums[i]
            result.append(nums[:])
            i = 1
            while p[i] == 0:
                p[i] = i
                i += 1
        return result
