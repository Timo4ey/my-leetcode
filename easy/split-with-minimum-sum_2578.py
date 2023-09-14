# Given a positive integer num, split it into two non-negative integers num1 and num2 such that:

# The concatenation of num1 and num2 is a permutation of num.
# In other words, the sum of the number of occurrences of each digit in num1 and num2 is equal to the number of occurrences of that digit in num.
# num1 and num2 can contain leading zeros.
# Return the minimum possible sum of num1 and num2.

# Notes:

# It is guaranteed that num does not contain any leading zeros.
# The order of occurrence of the digits in num1 and num2 may differ from the order of occurrence of num.


# Example 1:

# Input: num = 4325
# Output: 59
# Explanation: We can split 4325 so that num1 is 24 and num2 is 35, giving a sum of 59. We can prove that 59 is indeed the minimal possible sum.
# Example 2:

# Input: num = 687
# Output: 75
# Explanation: We can split 687 so that num1 is 68 and num2 is 7, which would give an optimal sum of 75.

# ---------------------------------------Runtime 32 ms Beats 92.78% Memory 16.1 MB Beats 99.48%---------------------------------------


from collections import deque


class Solution:
    def splitNum(self, num: int) -> int:
        arr = list(map(int, list(str(num))))
        arr.sort()
        arrNums = deque(arr)
        l = None
        r = None
        while arrNums:
            if l is None:
                l = arrNums.popleft()
            if r is None:
                r = arrNums.popleft()

            l = l + 0 if not arrNums else l * 10 + arrNums.popleft()
            r = r + 0 if not arrNums else r * 10 + arrNums.popleft()
        return l + r
