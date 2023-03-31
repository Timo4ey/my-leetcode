# https://leetcode.com/problems/is-subsequence/

# My solution


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        while count != len(s):
            for letter in t:
                if s[count] == letter:
                    count += 1
                if count >= len(s):
                    break
            break
        if count == len(s):
            return True
        return False


# Solution 392-solution-with-step-by-step-explanation
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # pointer for s
        j = 0  # pointer for t
        while i < len(s) and j < len(t):
            if s[i] == t[j]:  # if the characters match, move the pointer for s
                i += 1
            j += 1  # move the pointer for t regardless
        return i == len(s)  # if i has reached the end of s, s is a subsequence of t, else not





if __name__ == "__main__":
    solution = Solution()
    method = solution.isSubsequence
    s = "ace"
    t = "aec"
    print(method(s,t)) # False
    s = "abc"
    t = "ahbgdc"
    print(method(s,t)) # True
    s = "axc"
    t = "ahbgdc"
    print(method(s,t)) # False
    s = "b"
    t = "abc"
    print(method(s,t)) # True