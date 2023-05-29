# Given an array arr of integers, check if there exist two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

# Example 1:

# Input: arr = [10,2,5,3]
# Output: true
# Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
# Example 2:

# Input: arr = [3,1,7,11]
# Output: false
# Explanation: There is no i and j that satisfy the conditions.

# ---------------------------------------Runtime 93 msBeats 10.34% Memory 16.3 MB Beats 49.69%---------------------------------------

# My solution
# Complexity O(n^2)

class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j and arr[i] * 2 == arr[j]:
                    return True
        return False


# ---------------------------------------Runtime 70 ms Beats 43.95% Memory 16.4 MB Beats 14.46%---------------------------------------

# Solution @leihao1313
# Complexity O(n)
from collections import Counter


class Solution:

    def checkIfExist(self, arr: list[int]) -> bool:
        cnt = Counter(arr)
        return any(2 * x in cnt and x != 0 for x in arr) or cnt[0] > 1
