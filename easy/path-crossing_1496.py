# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

# Example 1:

# ￼
# Input: path = "NES"
# Output: false
# Explanation: Notice that the path doesn't cross any point more than once.
# Example 2:

# ￼
# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.


# Constraints:

# 1 <= path.length <= 104
# path[i] is either 'N', 'S', 'E', or 'W'.

# ---------------------------------------Runtime 38 ms Beats 57.97% Memory 17.3 MB Beats 5.49%---------------------------------------


class Point:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
        self.position = (x, y)

    def __sub__(self, other: "Point") -> "Point":
        return self.__class__(self.x - other.x, self.y - other.y)

    def __add__(self, other: "Point") -> "Point":
        return self.__class__(self.x + other.x, self.y + other.y)


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        current = Point()
        paths = {
            "N": Point(1, 1),
            "S": Point(-1, -1),
            "E": Point(y=1),
            "W": Point(y=-1),
        }
        visited = set()
        visited.add(current.position)

        for char in path:
            current = current + paths[char]
            if current.position in visited:
                return True
            visited.add(current.position)

        return False
