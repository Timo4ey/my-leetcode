# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

# Example 1:

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]

# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

# ---------------------------------------Runtime 912 ms Beats 34.14% Memory 19.8 MB Beats 67.36%---------------------------------------


from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left : right + 1])


# Solution @hiepit


class NumArray:
    def __init__(self, nums) -> None:
        self.preSum = nums
        for i in range(len(nums) - 1):
            self.preSum[i + 1] += self.preSum[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.preSum[right]
        return self.preSum[right] - self.preSum[left - 1]
