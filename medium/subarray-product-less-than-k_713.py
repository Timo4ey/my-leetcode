

# ---------------------------------------Runtime 670 ms Beats 87.44% Memory 19.7 MB Beats 14.26%---------------------------------------

# My solution 
# Time Complexity O(n)


class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:

        cur_window = 1
        output = left = 0
        if k > 1:
            for indx, value in enumerate(nums):
                cur_window *= value
                while cur_window >= k:
                    cur_window /= nums[left]
                    left += 1
                output += indx - left + 1
        return output
