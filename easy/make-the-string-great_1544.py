

# My solution

class Solution:
    def makeGood(self, s: str) -> str:
        stack = list(s)
        i, j = 0, 1
        while j <= len(stack) - 1:
            if (stack[i].isupper() and stack[i].lower() == stack[j]) or\
           (stack[j].isupper() and stack[i] == stack[j].lower()):
                stack.pop(i)
                stack.pop(i)
                if i:
                    i -= 1
                    j -= 1
            else:
                i += 1
                j += 1
        return ''.join(stack)