# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
# ---------------------------------------Runtime 51 ms Beats 12.1% Memory 16.3 MB Beats 10.96%---------------------------------------

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(":")","{":"}","[":"]",}
        stack = [0]
        for x in s:
            if x in brackets:
                stack.append(x)
            else:
                if brackets.get(stack.pop()) != x:
                    return False
        return stack == [0]
    
