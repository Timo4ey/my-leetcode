# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
# ---------------------------------------Runtime 234 ms Beats 5.8% Memory 17.3 MB Beats 32.95%---------------------------------------

# My solution
# Time complexity O(n log n)
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for i in range(len(numbers)):
            start, end = i + 1, len(numbers) - 1
            mb = numbers[i]
            while start <= end:
                middle = (start + end) // 2
                guess = numbers[middle] + mb
                if guess == target:
                    return [i + 1, middle + 1]
                elif guess > target:
                    end = middle - 1
                elif guess < target:
                    start = middle + 1

# ---------------------------------------Runtime 137 ms Beats 54.92% Memory 17.2 MB Beats 32.95%---------------------------------------

# Soltuion @constantine786
# Time - O(n)
# Space - O(1)
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers)-1

        while numbers[i] + numbers[j] != target:
            s = numbers[i] + numbers[j]
            if s > target:
                j -= 1
            else:
                i += 1

        return [i + 1, j + 1]
