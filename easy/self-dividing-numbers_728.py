# A self-dividing number is a number that is divisible by every digit it contains.

# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.

# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

# Example 1:

# Input: left = 1, right = 22
# Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
# Example 2:

# Input: left = 47, right = 85
# Output: [48,55,66,77]

# Constraints:

# 1 <= left <= right <= 104

# ---------------------------------------Runtime 58 ms Beats 16.21% Memory 16.52 MB Beats 59.93%---------------------------------------


from typing import List


class Solution:
    def is_bigger_then_ten(self, num: int) -> bool:
        return num >= 10

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res: List[int] = []
        for i in range(left, right + 1):
            nums: List[int] = []
            k = i
            while self.is_bigger_then_ten(k):
                k, r = divmod(k, 10)
                nums.append(r)
            not self.is_bigger_then_ten(k) and nums.append(k)
            flag = True
            for j in nums:
                flag = j != 0 and i % j == 0
                if not flag:
                    break
            flag and res.append(i)
        return res
