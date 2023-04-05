class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            midl = (start + end) // 2
            guess = nums[midl]
            if guess == target:
                return midl
            elif guess < target:
                start = midl + 1
            elif guess > target:
                end = midl - 1
        return -1
