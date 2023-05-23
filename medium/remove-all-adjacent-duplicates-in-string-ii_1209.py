
# You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal
# letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

# We repeatedly make k duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

# Example 1:

# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete.
# Example 2:

# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation: 
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"
# Example 3:

# Input: s = "pbbcggttciiippooaais", k = 2
# Output: "ps"

# ---------------------------------------Runtime 130 ms Beats 33.71% Memory 21.1 MB Beats 24.42%---------------------------------------

# My solution 1
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = list() # [character: str, amount: int]
        ans = ''
        for x in s:
            if stack and stack[-1][1] == k:
                stack.pop()
            if not stack:
                stack.append([x, 1])
            elif stack[-1][0] == x:
                stack[-1][1] += 1
            else:
                stack.append([x, 1])
        for j in stack:
            if j[1] != k:
                ans += j[0] * j[1]
        return ans

# ---------------------------------------Runtime125 ms Beats 39.40% Memory 21 MB Beats 24.42%---------------------------------------

# My solution 2
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = list() # [character: str, amount: int]
        ans = ''
        for x in s:
            if stack and stack[-1][0] == x:
                stack[-1][1] += 1
            else:
                stack.append([x, 1])
            if stack[-1][1] == k:
                stack.pop()
        return ''.join([c * i for c, i in stack])
