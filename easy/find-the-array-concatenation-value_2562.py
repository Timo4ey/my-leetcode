# You are given a 0-indexed integer array nums.

# The concatenation of two numbers is the number formed by concatenating their numerals.

# For example, the concatenation of 15, 49 is 1549.
# The concatenation value of nums is initially equal to 0. Perform this operation until nums becomes empty:

# If there exists more than one number in nums, pick the first element and last element in nums respectively and add the value of their concatenation to the concatenation value of nums, then delete the first and last element from nums.
# If one element exists, add its value to the concatenation value of nums, then delete it.
# Return the concatenation value of the nums.

# Example 1:

# Input: nums = [7,52,2,4]
# Output: 596
# Explanation: Before performing any operation, nums is [7,52,2,4] and concatenation value is 0.
#  - In the first operation:
# We pick the first element, 7, and the last element, 4.
# Their concatenation is 74, and we add it to the concatenation value, so it becomes equal to 74.
# Then we delete them from nums, so nums becomes equal to [52,2].
#  - In the second operation:
# We pick the first element, 52, and the last element, 2.
# Their concatenation is 522, and we add it to the concatenation value, so it becomes equal to 596.
# Then we delete them from the nums, so nums becomes empty.
# Since the concatenation value is 596 so the answer is 596.
# Example 2:

# Input: nums = [5,14,13,8,12]
# Output: 673
# Explanation: Before performing any operation, nums is [5,14,13,8,12] and concatenation value is 0.
#  - In the first operation:
# We pick the first element, 5, and the last element, 12.
# Their concatenation is 512, and we add it to the concatenation value, so it becomes equal to 512.
# Then we delete them from the nums, so nums becomes equal to [14,13,8].
#  - In the second operation:
# We pick the first element, 14, and the last element, 8.
# Their concatenation is 148, and we add it to the concatenation value, so it becomes equal to 660.
# Then we delete them from the nums, so nums becomes equal to [13].
#  - In the third operation:
# nums has only one element, so we pick 13 and add it to the concatenation value, so it becomes equal to 673.
# Then we delete it from nums, so nums become empty.
# Since the concatenation value is 673 so the answer is 673.

# ---------------------------------------Runtime 56 ms Beats 79.48% Memory 13.9 MB Beats 100%---------------------------------------


from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        stock = []
        while l < r:
            stock.append(int(f"{nums[l]}{nums[r]}"))
            l += 1
            r -= 1
        if l == r:
            stock.append(nums[l])
        return sum(stock)
