from functools import reduce



class List(list):
    ...




class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        def count_vowel(string):
            vowel = dict(zip(('a', 'e', 'i', 'o', 'u'), ('a', 'e', 'i', 'o', 'u')))
            if vowel.get(string[0]) and vowel.get(string[-1]):
                return 1
            return 0
        return reduce(lambda acc, x: acc + count_vowel(x), words[left:right + 1], 0)
    

sol = Solution()
print(sol.vowelStrings(words = ["are","amy","u"], left = 0, right = 2))
