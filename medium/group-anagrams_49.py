
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
# 
# ---------------------------------------Runtime 5223 ms Beats 5.1% Memory 22.1 MB Beats 8.52%---------------------------------------



class List(list):
    pass

# My solution 
# I tried don't use module collections, so that what i have

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_num_of_keys(items):
            output = {}
            for x in items:
                output[x] = output.get(x, 0) + 1
            return output
        items = []
        if strs:
            items.append([strs.pop(0)])
        i = 0
        length = len(strs) - 1
        while i <= length:
            temp_dict = get_num_of_keys(strs[i])
            z = 1
            while z <= length:
                if temp_dict == get_num_of_keys(strs[z]):
                    items[i].append(strs.pop(z))
                    z -= 1
                z += 1
                length = len(strs) - 1
            items.append([])
            i += 1
        if strs:
            items[len(items) - 1].append(strs[0])
        return items
    
# ---------------------------------------Runtime 109 ms Beats 52.30% Memory 20.3 MBBeats 15.98%---------------------------------------

# Solution @kitt

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters_to_words = defaultdict(list)
        for word in strs:
            letters_to_words[tuple(sorted(word))].append(word)
        return list(letters_to_words.values())