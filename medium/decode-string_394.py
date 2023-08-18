# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.


# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"

# ---------------------------------------Runtime 43 ms Beats 52.35% Memory 16.1 MB Beats 94.86%---------------------------------------


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        k = 0

        for char in s:
            if char == "[":
                stack.append((current_string, k))
                current_string = ""
                k = 0
            elif char == "]":
                last_string, last_k = stack.pop()
                current_string = last_string + last_k * current_string
            elif char.isdigit():
                k = k * 10 + int(char)
            else:
                current_string = f"{current_string}{char}"
        return current_string
