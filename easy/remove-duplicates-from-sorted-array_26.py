class List(list):
    ...


# My solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        while count < len(nums) - 1:
            if nums[count] == nums[count + 1]:
                del nums[count]
                count -= 1
            count += 1


s = Solution()
print(s.removeDuplicates([1, 1, 2]))
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
