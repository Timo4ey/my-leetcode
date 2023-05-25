# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
# ans[i] is the number of 1's in the binary representation of i.

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101


# ---------------------------------------Runtime 113 ms Beats 36.42% Memory 24.2 MB Beats 13.27%---------------------------------------

# My solution
# Time complexity O(n)

class Solution:
    def countBits(self, n: int) -> list[int]:
        store = []
        output = []
        for i in range(n + 1):
            store.append(str(bin(i)))
        for x in store:
            output.append(x.count('1'))
        return output


# Solution @jeffwei

class Solution:
    def countBits(self, num: int) -> list[int]:
        counter = [0]
        for i in range(1, num+1):
            counter.append(counter[i >> 1] + i % 2)
        return counter
