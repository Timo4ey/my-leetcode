from functools import reduce


class List(list):
    ...


# My solution 1


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        result = 0
        arr = words[left : right + 1]
        while count <= len(arr) - 1:
            vowel = dict(
                zip(("a", "e", "i", "o", "u"), ("a", "e", "i", "o", "u"))
            )
            if vowel.get(arr[count][0]) and vowel.get(arr[count][-1]):
                result += 1
            count += 1
        return result


# My solution 2
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        def count_vowel(string):
            vowel = dict(
                zip(("a", "e", "i", "o", "u"), ("a", "e", "i", "o", "u"))
            )
            if vowel.get(string[0]) and vowel.get(string[-1]):
                return 1
            return 0

        return reduce(
            lambda acc, x: acc + count_vowel(x), words[left : right + 1], 0
        )


# Solution Spaulding_
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = set("aeiou")

        return sum(
            {w[0], w[-1]}.issubset(vowels) for w in words[left : right + 1]
        )
