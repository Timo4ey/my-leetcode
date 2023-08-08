# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"
# ---------------------------------------Runtime 57 ms Beats 89.35% Memory 17.3 MB Beats 84.74%---------------------------------------


# Time complexity O(n)
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelsSet = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        point1 = 0
        point2 = len(s) - 1
        output = list(s)
        while point1 <= point2:
            p1 = output[point1]
            p2 = output[point2]
            if p1 in vowelsSet or p2 in vowelsSet:
                if output[point1] in vowelsSet and output[point2] in vowelsSet:
                    output[point1], output[point2] = (
                        output[point2],
                        output[point1],
                    )
                    point1 += 1
                    point2 -= 1
                elif (
                    output[point1] in vowelsSet
                    and output[point2] not in vowelsSet
                ):
                    point2 -= 1
                elif (
                    output[point2] in vowelsSet
                    and output[point1] not in vowelsSet
                ):
                    point1 += 1
            else:
                point1 += 1
                point2 -= 1
        return "".join(output)
