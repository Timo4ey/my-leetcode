# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


# ---------------------------------------Runtime 83 ms Beats 32.68% Memory 16.2 MB Beats 74.6%---------------------------------------

# DON'T USE CONVERSATION TO STRING
# Time complexity O(log n)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_num: int = 0
        y: int = x
        while y > 0:
            n, d = divmod(y, 10)
            new_num = new_num * 10 + d
            y = n
        return new_num == x
