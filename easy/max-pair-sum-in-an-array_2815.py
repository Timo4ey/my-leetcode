# You are given an integer array nums. You have to find the maximum sum of a pair of numbers from nums such that the largest digit in both numbers is equal.

# For example, 2373 is made up of three distinct digits: 2, 3, and 7, where 7 is the largest among them.

# Return the maximum sum or -1 if no such pair exists.


# Example 1:

# Input: nums = [112,131,411]

# Output: -1

# Explanation:

# Each numbers largest digit in order is [2,3,4].

# Example 2:

# Input: nums = [2536,1613,3366,162]

# Output: 5902

# Explanation:

# All the numbers have 6 as their largest digit, so the answer is 2536 + 3366 = 5902.

# Example 3:

# Input: nums = [51,71,17,24,42]

# Output: 88

# Explanation:

# Each number's largest digit in order is [5,7,7,4,4].

# So we have only two possible pairs, 71 + 17 = 88 and 24 + 42 = 66.


# Constraints:

# 2 <= nums.length <= 100
# 1 <= nums[i] <= 10^4

# ---------------------------------------Runtime 122 ms Beats 48.71% Memory 16.44 MB Beats 91.10%---------------------------------------


from typing import Dict, List


class Solution:

    @classmethod
    def _get_int_array_from_num(cls, num: int) -> List[int]:
        seen, nums = set(), []
        while num > 0:
            num, rest = divmod(num, 10)
            if rest not in seen:
                nums.append(rest)
                seen.add(rest)
        return nums

    @classmethod
    def _gather_nums(
        cls, nums: List[int], splitted_nums: List[List[int]]
    ) -> Dict[int, List[int]]:
        nums_map: Dict[int, List[int]] = dict()

        for num, num_arr in zip(nums, splitted_nums):
            m = max(num_arr)
            if m not in nums_map:
                nums_map[m] = [num]
            else:
                nums_map[m].append(num)

        return nums_map

    def maxSum(self, nums: List[int]) -> int:
        splitted_nums: List[List[int]] = [
            self._get_int_array_from_num(x) for x in nums
        ]
        nums_map: Dict[int, List[int]] = self._gather_nums(nums, splitted_nums)
        nested_nums = list(filter(lambda x: len(nums_map[x]) > 1, nums_map))

        max_num = -1
        for i in nested_nums:
            sorted_arrs: List[int] = sorted(nums_map[i], reverse=True)

            max_num = max(
                sum(map(lambda x: sorted_arrs[x], range(2))), max_num
            )
        return max_num
