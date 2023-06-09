class List(list):
    ...


# My solution


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        double = {}
        for i in nums:
            if double.get(i):
                return True
            double[i] = double.get(i, 0) + 1
        return False


s = Solution()
print(s.containsDuplicate([0, 4, 5, 0, 3, 6]))
print(s.containsDuplicate([1, 2, 3, 1]))
