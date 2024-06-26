# You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.

# Return the minimum number of operations to make all elements of nums divisible by 3.

# Example 1:

# Input: nums = [1,2,3,4]

# Output: 3

# Explanation:

# All array elements can be made divisible by 3 using 3 operations:

# Subtract 1 from 1.
# Add 1 to 2.
# Subtract 1 from 4.
# Example 2:

# Input: nums = [3,6,9]

# Output: 0

# Constraints:

# 1 <= nums.length <= 50
# 1 <= nums[i] <= 50


# ---------------------------------------Runtime 40 ms Beats 59.94% Memory 16.47 MB Beats 82.10%---------------------------------------


from typing import List


class Solution:
    def make_divisible_by_three(self, num: int) -> int:
        res = 0
        while num % 3 != 0:
            if (num - 1) % 3 == 0:
                num = num - 1
            else:
                num = num + 1
            res += 1

        return res

    def minimumOperations(self, nums: List[int]) -> int:
        return sum(self.make_divisible_by_three(num) for num in nums)
