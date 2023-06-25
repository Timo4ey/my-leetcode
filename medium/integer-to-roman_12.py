class Solution:
    def intToRoman(self, num: int) -> str:
        ans: list = []
        roman: list = ["I", "IV", "V", "IX", "X", "XL",
                       "L", "XC", "C", "CD", "D", "CM", "M"]
        nums: list = [1, 4, 5, 9, 10, 40, 50, 90,
                100, 400, 500, 900, 1000]

        i: int = len(nums) - 1

        while num:
            div, num = divmod(num, nums[i])

            while div:
                ans.append(roman[i])
                div -= 1
            i -= 1
        return "".join(ans)
