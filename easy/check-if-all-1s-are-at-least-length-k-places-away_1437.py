# Given an binary array nums and an integer k, return true if all 1's are at
# least k places away from each other, otherwise return false.

# Example 1:

# ￼
# Input: nums = [1,0,0,0,1,0,0,1], k = 2
# Output: true
# Explanation: Each of the 1s are at least 2 places away from each other.
# Example 2:

# ￼
# Input: nums = [1,0,0,1,0,1], k = 2
# Output: false
# Explanation: The second 1 and third 1 are only one apart from each other.

# ---------------------------------------Runtime 559 ms Beats 49.41% Memory 22.3 MB Beats 7.99%---------------------------------------


# My Solution 1
# Time Complexity O(n)
class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        units = [x for x in range(len(nums)) if nums[x] == 1]

        for x in range(len(units) - 1):
            if units[x + 1] - units[x] <= k:
                return False
        return True


# ---------------------------------------Runtime 559 ms Beats 49.41% Memory 22.2 MB Beats 8.88%---------------------------------------


# My Solution 1
# Time Complexity O(n)
class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        units = [x for x in range(len(nums)) if nums[x] == 1]
        return all(
            map(
                lambda x: False if units[x + 1] - units[x] <= k else True,
                range(len(units) - 1),
            )
        )
