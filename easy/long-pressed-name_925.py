# Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

# You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.


# Example 1:

# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.
# Example 2:

# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it was not in the typed output.


# Constraints:

# 1 <= name.length, typed.length <= 1000
# name and typed consist of only lowercase English letters.

# ---------------------------------------Runtime 40 ms Beats 28.91% Memory 16.38 MB Beats 97.35%---------------------------------------


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if typed[0] != name[0]:
            return False

        l_name = len(name)
        l_typed = len(typed)

        i = j = 0

        prev_n = None
        while i < l_name and j < l_typed:
            n = name[i]
            t = typed[j]
            if n == t:
                i += 1
                j += 1
                prev_n = n
            elif n != t and t == prev_n:
                j += 1
            else:
                i = 0
                j += 1
                prev_n = None
        s = set(typed[j:])
        if not i == l_name:
            return False
        return (
            not typed[j:]
            or typed[j:]
            and len(s) == 1
            and s.pop() == name[-1]
            or False
        )
