# You are given a string num representing a large integer. An integer is good if it meets the following conditions:

# It is a substring of num with length 3.
# It consists of only one unique digit.
# Return the maximum good integer as a string or an empty string "" if no such integer exists.

# Note:

# A substring is a contiguous sequence of characters within a string.
# There may be leading zeroes in num or a good integer.


# Example 1:

# Input: num = "6777133339"
# Output: "777"
# Explanation: There are two distinct good integers: "777" and "333".
# "777" is the largest, so we return "777".
# Example 2:

# Input: num = "2300019"
# Output: "000"
# Explanation: "000" is the only good integer.
# Example 3:

# Input: num = "42352338"
# Output: ""
# Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.


# ---------------------------------------Runtime 51 ms Beats 14.6% Memory 16.3 MB Beats 59.27%---------------------------------------


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num) - 1
        res = ""

        for i in range(n):
            j = i + 1
            while j <= n and num[i] == num[j]:
                if j - i == 2:
                    res = max(
                        res or "000", num[i : j + 1], key=lambda x: int(x)
                    )
                    break
                j += 1
        return res
