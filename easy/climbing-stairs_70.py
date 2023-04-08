class Solution:
    def climbStairs(self, N: int) -> int:
        counter = 0
        def fib(N: int) -> int:
            a, b = 0, 1
            for i in range(N): a, b = b, a + b
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
