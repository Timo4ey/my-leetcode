# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.


# Example 1:

# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
# Example 2:

# Input: n = 1, bad = 1
# Output: 1

# ---------------------------------------Runtime 36 ms Beats 70.15% Memory 16 MB Beats 93.78%---------------------------------------


class isBadVersion:
    ...


# My solution
class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0
        finish = n
        results = []
        while start <= finish:
            midl = (start + finish) // 2
            result = isBadVersion(midl)
            if result:
                results.append(midl)
                finish = midl - 1
            else:
                start = midl + 1
        return min(results)


#  MVP
# class Solution:
#     def firstBadVersion(self, n: int) -> int:
#         start = 0
#         finish = n
#         results = []
#         for x in range(n,0, -1):
#             if isBadVersion(x):
#                 results.append(x)
#         return min(results)


# Solution GANJINAVEEN


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid) == False:
                left = mid + 1
            else:
                right = mid - 1
        return left


class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0
        finish = n
        results = {}
        while start <= finish:
            midl = (start + finish) // 2
            result = isBadVersion(midl)
            if result:
                results[midl] = midl
                finish = midl - 1
            else:
                start = midl + 1
        return min(results, key=results.get)
