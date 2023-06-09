# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.


# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
# ---------------------------------------Runtime 231 ms Beats 8.28% Memory 20.7 MB Beats 15.24%---------------------------------------


class List(list):
    pass


# My solution


class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s) - 1
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1


# ---------------------------------------Runtime 222 ms Beats 18.56% Memory 20.8  MB Beats 8.40%---------------------------------------

# Solution @Movely


class Solution:
    def reverseString(self, s):
        for i in range(len(s) // 2):
            s[i], s[~i] = s[~i], s[i]
