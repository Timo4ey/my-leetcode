# 409. Longest Palindrome

# MY solution 

class Solution:
    def longestPalindrome(self, s: str) -> int:
        temp_dict = {}
        perform_dict = {}
        for x in s:
            if not temp_dict.get(x):
                temp_dict[x] = 1
            elif temp_dict.get(x) and not perform_dict.get(x):
                del temp_dict[x]
                perform_dict[x] = 2
            elif temp_dict.get(x) and perform_dict.get(x):
                del temp_dict[x]
                perform_dict[x] += 2
        output = sum(perform_dict.values())
        if temp_dict:
            return output + 1
        return output


# Solution from Editorial
# 
import collections


class Solution:
    def longestPalindrome(self, s):
        ans = 0
        for v in collections.Counter(s).itervalues():
            ans += v / 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans