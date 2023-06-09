# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
# ---------------------------------------Runtime 6037 ms Beats 10.37% Memory 21.6 MB Beats 5.16%---------------------------------------
# My Solution 1
# Time complexity O(n2)


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        lenght = len(nums)
        ans = {}
        nums.sort()
        for i in range(lenght):
            j, k = i + 1, lenght - 1
            while j < k:
                guess = [nums[i], nums[j], nums[k]]
                _sum = sum(guess)
                if _sum == 0:
                    ans[tuple(set(guess))] = guess
                if _sum > 0:
                    k -= 1
                else:
                    j += 1
        return list(ans.values())


# ---------------------------------------Runtime 2223 ms Beats 33.75% Memory 20.6 MB Beats 24.60%---------------------------------------
# My Solution 2
# Time complexity O(n2)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                guess = [nums[i], nums[j], nums[k]]
                _sum = sum(guess)
                if _sum > 0:
                    k -= 1
                elif _sum < 0:
                    j += 1
                else:
                    ans.append(guess)
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return ans


# Solution @Mangosteen
# Time complexity O(n2)


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        result = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            target = 0 - nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return list(result)
