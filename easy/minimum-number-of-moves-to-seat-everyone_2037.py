# There are n seats and n students in a room. You are given an array seats of length n, where seats[i] is the position of the ith seat. 
# You are also given the array students of length n, where students[j] is the position of the jth student.

# You may perform the following move any number of times:

# Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from position x to x + 1 or x - 1)
# Return the minimum number of moves required to move each student to a seat such that no two students are in the same seat.

# Note that there may be multiple seats or students in the same position at the beginning.
# Example 1:

# Input: seats = [3,1,5], students = [2,7,4]
# Output: 4

# Example 2:
# Input: seats = [4,1,5,9], students = [1,3,2,6]
# Output: 7.

# Example 3:
# Input: seats = [2,2,6,6], students = [1,3,2,6]
# Output: 4
 
# Constraints:

# n == seats.length == students.length
# 1 <= n <= 100
# 1 <= seats[i], students[j] <= 100

# ---------------------------------------Runtime 67 ms Beats 51.12% Memory 13.9 MB Beats 57.33%--------------------------------------------------------------------------------------
from functools import reduce



class List(list):
    pass


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        return reduce(lambda acc, x: acc + abs(x[0] - x[1]), zip(seats, students), 0)
