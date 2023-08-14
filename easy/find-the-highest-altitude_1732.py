# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.


# Example 1:

# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
# Example 2:

# Input: gain = [-4,-3,-2,-1,4,3,2]
# Output: 0
# Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.


# ---------------------------------------Runtime 40 ms Beats 93.90% Memory 16.3 MB Beats 69.76%---------------------------------------

# Time complexity O(n)


class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        gain = [0] + gain
        for i in range(1, len(gain)):
            gain[i] = gain[i - 1] + gain[i]
        return max(gain)
