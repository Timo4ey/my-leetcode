# Given a string s, reverse the string according to the following rules:

# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.


# Example 1:

# Input: s = "ab-cd"
# Output: "dc-ba"
# Example 2:

# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:

# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"


# Constraints:

# 1 <= s.length <= 100
# s consists of characters with ASCII values in the range [33, 122].
# s does not contain '\"' or '\\'.

# ---------------------------------------Runtime 48 ms Beats 10.56% Memory 16.3 MB Beats 12.98%---------------------------------------


# My solution
from string import ascii_letters


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        arr = list(s)
        letters = dict(zip(ascii_letters, ascii_letters))
        while l < r:
            if letters.get(arr[l]) and letters.get(arr[r]):
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            elif (
                letters.get(arr[l]) is None and letters.get(arr[r]) is not None
            ):
                l += 1
                if letters.get(arr[l]):
                    arr[l], arr[r] = arr[r], arr[l]
                    l += 1
                    r -= 1
            elif (
                letters.get(arr[r]) is None and letters.get(arr[l]) is not None
            ):
                r -= 1
                if letters.get(arr[r]):
                    arr[l], arr[r] = arr[r], arr[l]
                    l += 1
                    r -= 1
            else:
                l += 1
                r -= 1
        return "".join(arr)


sol = Solution()


# Solution @lee215

# ---------------------------------------Runtime 42 ms Beats 19.78% Memory 16.3 MB Beats 12.98%-------------------------------------------------------------------------


def reverseOnlyLetters(self, S):
    S, i, j = list(S), 0, len(S) - 1
    while i < j:
        if not S[i].isalpha():
            i += 1
        elif not S[j].isalpha():
            j -= 1
        else:
            S[i], S[j] = S[j], S[i]
            i, j = i + 1, j - 1
    return "".join(S)
