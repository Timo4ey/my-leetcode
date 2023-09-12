# connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.


# Example 1:

# ￼
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:

# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3

# ---------------------------------------Runtime 212 ms Beats 55.25% Memory 17.7 MB Beats 8.58%---------------------------------------


# Time complexity O(n^2)
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        def dfs(start):
            visited.add(start)
            for end in range(len(isConnected)):
                if isConnected[start][end] and end not in visited:
                    dfs(end)

        visited = set()
        num_of_provinces = 0
        for start in range(len(isConnected)):
            if start not in visited:
                num_of_provinces += 1
                dfs(start)
        return num_of_provinces
