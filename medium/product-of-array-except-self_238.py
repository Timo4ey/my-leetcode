# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
# ---------------------------------------Runtime 181 ms Beats 99.1% Memory 24.1 MB Beats 45.35%---------------------------------------

# Time Complexity O(n)


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        # Create an same size array
        sol = [1] * length
        # Declare previous num to use it
        previous_num = 1
        post_num = 1
        for i in range(length):
            sol[i] *= previous_num
            previous_num = previous_num * nums[i]
            sol[length - i - 1] *= post_num
            post_num = post_num * nums[length - i - 1]

        return sol
