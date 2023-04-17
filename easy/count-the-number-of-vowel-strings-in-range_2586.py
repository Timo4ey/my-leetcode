class List(list):
    ...


# My solution

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        result = 0
        arr = words[left:right + 1]
        while count <= len(arr):
            vowel = dict(zip(('a', 'e', 'i', 'o', 'u'), ('a', 'e', 'i', 'o', 'u')))
            if vowel.get(arr[count][0]) and vowel.get(arr[count][-1]):
                result += 1
            count += 1
        return result

    

# Solution Spaulding_
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:

        vowels = set('aeiou')
        
        return sum({w[0],w[-1]}.issubset(vowels) for w in words[left:right+1])
