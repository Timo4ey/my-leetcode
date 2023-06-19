# Given the array nums, for each nums[i] find out how many numbers in
# the array are smaller than it.
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

# Return the answer in an array.

# Example 1:

# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation:
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1).
# For nums[3]=2 there exist one smaller number than it (1).
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
# Example 2:

# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]
# Example 3:

# Input: nums = [7,7,7,7]
# Output: [0,0,0,0]

# ---------------------------------------Runtime 74 ms Beats 78.42% Memory 16.3 MB Beats 56.60%---------------------------------------

# My solution
# Time Complexity O(n log n)


class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        # sort the list to be aware the current num is less then the next num
        temp: list = sorted(nums)
        # dict for gathering nums in their indexies
        # index is equal how many numbers are smaller
        map_dict: dict = {}
        ans: list = []
        # get values and their indexes
        for i, j in enumerate(temp):
            if j not in map_dict:
                map_dict[j] = i
        # get indexes
        for i in nums:
            ans.append(map_dict[i])
        return ans
