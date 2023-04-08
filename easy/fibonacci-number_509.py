
# My solution

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
    


# Solution junaidmansuri

class Solution:
    def fib(self, N: int) -> int:
    	a, b = 0, 1
        for i in range(N): a, b = b, a + b
    	return a
    
