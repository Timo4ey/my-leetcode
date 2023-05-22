# You are given a string s consisting of lowercase English letters.
# A duplicate removal consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

# Example 1:

# Input: s = "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
# Example 2:

# Input: s = "azxxzy"
# Output: "ay"

# ---------------------------------------Runtime 515 ms Beats 5.3% Memory 17.1 MB Beats 24.43%---------------------------------------

# Type: Stack


from functools import reduce

# My solution 1
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = list(s)
        i = 0
        r = 1
        while r <= len(stack) - 1:
            num1 = stack[i]
            num2 = stack[r]
            if num1 == num2:
                stack.pop(i)
                stack.pop(i)
                if i:
                    i -= 1
                    r -= 1
            else:
                i += 1
                r += 1

        return ''.join(stack)

# My solution 2
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            if stack[-1][1] == 2:
                stack.pop()
        return ''.join([c for c, i in stack])

# Solution @lee215
class Solution:
    def removeDuplicates(self, S):
        return reduce(lambda s, c: s[:-1] if s[-1:] == c else s + c, S)
