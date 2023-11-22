# We define the conversion array conver of an array arr as follows:

# conver[i] = arr[i] + max(arr[0..i]) where max(arr[0..i]) is the maximum value of arr[j] over 0 <= j <= i.
# We also define the score of an array arr as the sum of the values of the conversion array of arr.

# Given a 0-indexed integer array nums of length n, return an array ans of length n where ans[i] is the score of the prefix nums[0..i].

# Example 1:

# Input: nums = [2,3,7,5,10]
# Output: [4,10,24,36,56]
# Explanation:
# For the prefix [2], the conversion array is [4] hence the score is 4
# For the prefix [2, 3], the conversion array is [4, 6] hence the score is 10
# For the prefix [2, 3, 7], the conversion array is [4, 6, 14] hence the score is 24
# For the prefix [2, 3, 7, 5], the conversion array is [4, 6, 14, 12] hence the score is 36
# For the prefix [2, 3, 7, 5, 10], the conversion array is [4, 6, 14, 12, 20] hence the score is 56
# Example 2:

# Input: nums = [1,1,2,4,8,16]
# Output: [2,4,8,16,32,64]
# Explanation:
# For the prefix [1], the conversion array is [2] hence the score is 2
# For the prefix [1, 1], the conversion array is [2, 2] hence the score is 4
# For the prefix [1, 1, 2], the conversion array is [2, 2, 4] hence the score is 8
# For the prefix [1, 1, 2, 4], the conversion array is [2, 2, 4, 8] hence the score is 16
# For the prefix [1, 1, 2, 4, 8], the conversion array is [2, 2, 4, 8, 16] hence the score is 32
# For the prefix [1, 1, 2, 4, 8, 16], the conversion array is [2, 2, 4, 8, 16, 32] hence the score is 64

# ---------------------------------------Runtime 552 ms Beats 5.11% Memory 36.7 MB Beats 75.81%---------------------------------------


from itertools import accumulate
from typing import List


# My solution
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        # define current maximum
        cur_mx = nums[0]
        # get first element that the func `max` doesn't return
        # an error 'ValueError: max() arg is an empty sequence'
        sum_ = nums[0] * 2
        # put our sum into list
        ans = [sum_]
        for i in range(1, len(nums)):
            # get max number for sum the next element num[0...i]
            cur_mx = max(cur_mx, nums[i])
            # sum elements
            sum_ += cur_mx + nums[i]
            ans.append(sum_)
        return ans


# Solution SunnyvaleCA
def findPrefixScore(self, A):
    return accumulate(n + maxN for n, maxN in zip(A, accumulate(A, max)))


sol = Solution()
nums = [2, 3, 7, 5, 10]
print(sol.findPrefixScore(nums))
nums = [1, 1, 2, 4, 8, 16]
print(sol.findPrefixScore(nums))


# My solution with bad time


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        output = []
        count = 0
        while count <= len(nums) - 1:
            output.append(nums[count] + max(nums[: count + 1]))
            count += 1
        count = 0
        while count <= len(output) - 1:
            mx = 0
            if output[:count]:
                mx = max(output[:count])
            output[count] = output[count] + mx
            count += 1
        return output
