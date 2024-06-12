# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.

# Follow up: Could you come up with a one-pass algorithm using only constant extra space?


# ---------------------------------------Runtime 32 ms Beats 85.64% Memory 16.42 MB Beats 79.02%---------------------------------------


from typing import List


class Solution:
    def count_sort(self, input_array: list[int]) -> List[int]:
        max_costs: int = max(input_array)
        countArray: List[int] = [0] * (max_costs + 1)
        n: int = len(input_array)
        for cost in input_array:
            countArray[cost] += 1

        for i in range(1, max_costs + 1):
            countArray[i] += countArray[i - 1]
        output_array: List[int] = [0] * n

        for i in range(n - 1, -1, -1):
            output_array[countArray[input_array[i]] - 1] = input_array[i]
            countArray[input_array[i]] -= 1
        return output_array

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ns = self.count_sort(nums)
        nums.clear()
        nums.extend(ns)
