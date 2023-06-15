# Given a 2D integer array nums where nums[i] is a non-empty array of distinct
# positive integers, return the list of integers that are present in each array of nums sorted in ascending order.


# Example 1:

# Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
# Output: [3,4]
# Explanation: 
# The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].
# Example 2:

# Input: nums = [[1,2,3],[4,5,6]]
# Output: []
# Explanation: 
# There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].

# ---------------------------------------Runtime 81 ms Beats 67.36% Memory 16.9 MB Beats 18.9%---------------------------------------

# My solution
# Time Complexity O(n log n)

class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        ans: set = set(nums[0])
        for i in range(1, len(nums)):
            ans = ans.intersection(nums[i])
        return sorted(ans)


# Solution @lee215

class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        return sorted(set.intersection(*map(set, nums)))
