# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


# https://leetcode.com/problems/two-sum/
# My solution

# Time complexity: O(N^2);
# Space Complexity: O(1);

# ---------------------------------------Runtime  7503 ms Beats 5% Memory 15 MB Beats 100%---------------------------------------


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for indx, num in enumerate(nums):
            for indx2, num2 in enumerate(nums):
                if indx != indx2 and num + num2 == target:
                    return [indx, indx2]


# Optimized Code

# Time complexity: O(N);
# Space Complexity: O(N);


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numToIndex = {}
        for i in range(len(nums)):
            if target - nums[i] in numToIndex:
                return [numToIndex[target - nums[i]], i]
            numToIndex[nums[i]] = i
        return []


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([1, 2, 1, 8, 10, 3, 2, 3, 1, 2, 3, 4], 6))
