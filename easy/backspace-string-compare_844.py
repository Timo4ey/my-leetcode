# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# Example 3:

# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".

# ---------------------------------------Runtime 42 ms Beats 35.16% Memory 16.3 MB Beats 11.27%---------------------------------------

# My solution


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def cut_of(array: list):
            stack = []
            for i in range(len(array)):
                val = array[i]
                if val != "#":
                    stack.append(val)
                elif val == "#":
                    if stack:
                        stack.pop()
            return stack

        return cut_of(s) == cut_of(t)


# Solution lee215
# Follow up: O(1) Space

from functools import reduce


class Solution:
    def backspaceCompare(self, S, T):
        back = lambda res, c: res[:-1] if c == "#" else res + c
        return reduce(back, S, "") == reduce(back, T, "")


if __name__ == "__main__":
    sol = Solution()
    s = "ab#c"
    t = "ad#c"
    print(sol.backspaceCompare(s, t))
    s = "ab##"
    t = "c#d#"
    print(sol.backspaceCompare(s, t))

    s = "a#c"
    t = "b"
    print(sol.backspaceCompare(s, t))

    s = "a#c"
    t = "a#b"
    print(sol.backspaceCompare(s, t))

    s = "a##c"
    t = "#a#c"
    print(sol.backspaceCompare(s, t))

# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         s1 = deque(s)
#         t1 = deque(t)
#         for s,e in zip(s, s):
#             if e == '#':
#                 s1.popleft()
#         for s,e in zip(t, t):
#             if e == '#':
#                 t1.popleft()
#         print(s1, t1)
#         return s1 == t1


# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         s1 = deque(s)
#         t1 = deque(t)
#         def cut_of(array: list):
#             output = []
#             start = 0
#             end = len(array) - 1
#             while end >= start:
#                 if array[end] != '#':
#                     output.append(array[start])

#                 start += 1
#                 end -= 1
#             return output
#         return cut_of(s) == cut_of(t)
