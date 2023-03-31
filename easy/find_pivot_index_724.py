# https://leetcode.com/problems/find-pivot-index/
# My solution

List = list


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i + 1:]):
                return i
        return -1


# Solution very-easy-100-fully-explained-java-c-python-js-python3

# Time Complexity : O(n)
# Space Complexity : O(1)
class Solution(object):
    def pivotIndex(self, nums):
        # Initialize leftSum & rightSum to store the sum of all the numbers strictly to the index's left & right respectively...
        leftSum, rightSum = 0, sum(nums)
        # Traverse elements through the loop...
        for idx, ele in enumerate(nums):
            rightSum -= ele
            # If the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right...
            if leftSum == rightSum:
                return idx      # Return the pivot index...
            leftSum += ele
        return -1       # If there is no index that satisfies the conditions in the problem statement...



if __name__ == "__main__":
    s = Solution()
    print(s.pivotIndex([1,7,3,6,5,6])) # 3
    print(s.pivotIndex([1,2,3])) # -1
    print(s.pivotIndex([2,1,-1])) # 0



