class List(list):
    ...


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        stock = []
        while l < r:
            stock.append(int(f"{nums[l]}{nums[r]}"))
            l += 1
            r -= 1
        if l == r:
            stock.append(nums[l])
        return sum(stock)
