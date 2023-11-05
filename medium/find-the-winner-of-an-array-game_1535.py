# Given an integer array arr of distinct integers and an integer k.

# A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0, and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.

# Return the integer which will win the game.

# It is guaranteed that there will be a winner of the game.

# Example 1:

# Input: arr = [2,1,3,5,4,6,7], k = 2
# Output: 5
# Explanation: Let's see the rounds of the game:
# Round |       arr       | winner | win_count
#   1   | [2,1,3,5,4,6,7] | 2      | 1
#   2   | [2,3,5,4,6,7,1] | 3      | 1
#   3   | [3,5,4,6,7,1,2] | 5      | 1
#   4   | [5,4,6,7,1,2,3] | 5      | 2
# So we can see that 4 rounds will be played and 5 is the winner because it wins 2 consecutive games.
# Example 2:

# Input: arr = [3,2,1], k = 10
# Output: 3
# Explanation: 3 will win the first 10 rounds consecutively.


# ---------------------------------------Runtime 527 ms Beats 65.76% Memory 30.6 MB Beats 11.41%---------------------------------------

from collections import deque


class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:
        d_arr, max_num, counter = deque(arr), max(arr), 0

        while counter < k:
            num_1, num_2 = d_arr.popleft(), d_arr.popleft()
            if num_1 == max_num or num_2 == max_num:
                return max(num_1, num_2)

            if num_1 > num_2:
                d_arr.append(num_2)
                d_arr.appendleft(num_1)
                counter += 1
            else:
                d_arr.append(num_1)
                d_arr.appendleft(num_2)
                counter = 1

        return d_arr.popleft()
