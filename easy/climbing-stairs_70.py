# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# ---------------------------------------Runtime 39 ms Beats 46.60% Memory 13.8 MB Beats 100%---------------------------------------


class Solution:
    def climbStairs(self, N: int) -> int:
        counter = 0

        def fib(N: int) -> int:
            a, b = 0, 1
            for i in range(N):
                a, b = b, a + b
            return a

        for i in range(N):
            counter += fib(i)
        return counter + 1


s = Solution()
print(s.climbStairs(40))

# 2 -> 1, 1 or 2
# 3 -> 1, 1,1 or 2 + 1 or 1 + 2
# 4 ->
#       1, 1, 1, 1
#       or 2 + 2
#       or 2 + 1 + 1
#       or 1 + 2 + 1
#       or 1 + 1 + 2
#
