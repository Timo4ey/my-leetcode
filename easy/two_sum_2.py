# https://leetcode.com/problems/two-sum/
# My solution

# Time complexity: O(N^2);
# Space Complexity: O(1);


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for indx, num in enumerate(nums):
            for indx2, num2 in enumerate(nums):
                if indx != indx2 and num + num2 == target:
                    return [indx, indx2]


# Optimized Code

# Time complexity: O(N);
# Space Complexity: O(N);


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numToIndex = {}
        for i in range(len(nums)):
            if target - nums[i] in numToIndex:
                return [numToIndex[target - nums[i]], i]
            numToIndex[nums[i]] = i
        return []


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([1, 2, 1, 8, 10, 3, 2, 3, 1, 2, 3, 4], 6))
