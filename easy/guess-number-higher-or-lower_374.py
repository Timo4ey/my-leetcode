# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:

# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.


# Example 1:

# Input: n = 10, pick = 6
# Output: 6
# Example 2:

# Input: n = 1, pick = 1
# Output: 1
# Example 3:

# Input: n = 2, pick = 1
# Output: 1

# ---------------------------------------Runtime 31 ms Beats 91.16% Memory 16.3 MB Beats 61.6%---------------------------------------


def guess(num: int) -> int:
    """Implementation"""


class Solution:
    def guessNumber(self, n: int) -> int:
        start, end = 0, n
        while start <= end:
            middle = (start + end) // 2
            g = guess(middle)
            if g == 0:
                return middle
            if g == -1:
                end = middle - 1
            if g == 1:
                start = middle + 1
