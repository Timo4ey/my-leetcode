# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.


# Example 1:

# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:

# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# Example 3:

# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
# ---------------------------------------Runtime 449 ms Beats 22.70% Memory 19 MB Beats 82.55%---------------------------------------

# Time complexity O(n)


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        zero_count = 0
        window_count = 0

        start = 0

        for i in range(len(nums)):
            zero_count += 1 if nums[i] == 0 else 0

            while zero_count > 1:
                zero_count -= 1 if nums[start] == 0 else 0
                start += 1

            window_count = max(window_count, i - start)
        return window_count
