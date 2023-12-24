# It is a sweltering summer day, and a boy wants to buy some ice cream bars.

# At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible.

# Note: The boy can buy the ice cream bars in any order.

# Return the maximum number of ice cream bars the boy can buy with coins coins.

# You must solve the problem by counting sort.


# Example 1:

# Input: costs = [1,3,2,4,1], coins = 7
# Output: 4
# Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.
# Example 2:

# Input: costs = [10,6,8,7,7,8], coins = 5
# Output: 0
# Explanation: The boy cannot afford any of the ice cream bars.
# Example 3:

# Input: costs = [1,6,3,1,2,5], coins = 20
# Output: 6
# Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.


# Constraints:

# costs.length == n
# 1 <= n <= 105
# 1 <= costs[i] <= 105
# 1 <= coins <= 108

# ---------------------------------------Runtime 756 ms Beats 13.4% Memory 31.3 MB Beats 6.5%---------------------------------------

from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        def count_sort(input_array: list[int]):
            max_costs = max(input_array)
            countArray = [0] * (max_costs + 1)
            n = len(input_array)
            for cost in input_array:
                countArray[cost] += 1

            for i in range(1, max_costs + 1):
                countArray[i] += countArray[i - 1]
            output_array = [0] * n

            for i in range(n - 1, -1, -1):
                output_array[countArray[input_array[i]] - 1] = input_array[i]
                countArray[input_array[i]] -= 1
            return output_array

        new_arr = count_sort(costs)

        ans = 0

        for num in new_arr:
            coins -= num
            if coins >= 0:
                ans += 1
            else:
                break
        return ans
