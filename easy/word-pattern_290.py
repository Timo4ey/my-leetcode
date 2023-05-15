# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
# ---------------------------------------Runtime 40 ms Beats 30.6% Memory 16.3 MB Beats 7.37%---------------------------------------

# My solution
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        array: list[dict] = []
        data = s.split()
        if len(pattern) != len(data):
            return False
        for patt,string in zip(pattern, data):
            array.append({patt: string})
        
        for x in array:
            (key,) = *x.keys(),
            (val,) = *x.values(),
            if dic.get(key) and dic.get(key) != val:
                return False
            if not dic.get(key) and val in dic.values():
                return False
            if not dic.get(key):
                dic[key] = val
        return True

 
# ---------------------------------------Runtime 43 ms Beats 25.3% Memory 16.3 MB Beats 24.56%---------------------------------------

# Solution @StefanPochmann
class Solution:
    def wordPattern(self, pattern, str):
        s = pattern
        t = str.split()
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)