# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.


# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1
# ---------------------------------------Runtime 123 ms Beats 99.58% Memory 19.1 MB Beats 53.40%---------------------------------------


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        seen = dict()
        for i in nums:
            seen[i] = seen.get(i, 0) + 1
        return min(seen, key=seen.get)
