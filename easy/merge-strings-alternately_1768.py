
# My solution
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ''
        l = 0
        r = 0
        while l < len(word1) or r < len(word2):
            if  l == len(word1):
                output += word2[r:]
                return output
            if  r == len(word2):
                output +=word1[l:]
                return output
            
            output += f'{word1[l]}{word2[r]}'
            l += 1
            r += 1
        return output
