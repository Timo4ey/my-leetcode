# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# ---------------------------------------Runtime 72 ms Beats 17% Memory 22.4 MB Beats 5.10%---------------------------------------

# My solution 1 "Two pointers"
class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''.join(list(map(lambda x: x.lower() if x.isalpha() or x.isalnum()
else '', s)))
        l, r = 0, len(st) - 1
        while l <= r:
            if st[l] != st[r]:
                return False
            l += 1
            r -= 1
        return True

# My solution 2
# ---------------------------------------Runtime 70 ms Beats 19.51% Memory 22.5 MB Beats 5.10%---------------------------------------

from string import ascii_letters


class Solution:
    def isPalindrome(self, s: str) -> bool:
        alph = set(ascii_letters + '1234567890')
        st = ''.join(list(map(lambda x: x.lower() if x in alph else "", s)))
        return st == st[::-1]
