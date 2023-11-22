# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

# ---------------------------------------Runtime 622 msBeats 46.54% Memory 29.6 MB Beats 18.53%---------------------------------------


from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        temp_dict = dict()

        def add_to_dict(values: tuple, a_dict: dict):
            a_dict[values[1]] = values[0]

        return any(
            filter(
                lambda x: True
                if x[1] in temp_dict and x[0] - temp_dict[x[1]] <= k
                else add_to_dict(x, temp_dict),
                enumerate(nums),
            )
        )
