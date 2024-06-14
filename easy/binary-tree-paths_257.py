# You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

# Return the minimum number of moves to make every value in nums unique.

# The test cases are generated so that the answer fits in a 32-bit integer.

# Example 1:

# Input: nums = [1,2,2]
# Output: 1
# Explanation: After 1 move, the array could be [1, 2, 3].
# Example 2:

# Input: nums = [3,2,1,2,1,7]
# Output: 6
# Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
# It can be shown with 5 or less moves that it is impossible for the array to have all unique values.

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 105

# ---------------------------------------Runtime 35 ms Beats 69.55% Memory 16.50 MB Beats 79.94%---------------------------------------

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def concat_nums(self, num: int, prev: str = None) -> str:
        res: str = f"{num}"
        if prev:
            res = f"{prev}->{num}"
        return res

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res = []

        def dfs(node: Optional[TreeNode], path: str = "") -> None:
            concat: str = node and self.concat_nums(node.val, path) or ""
            node and not node.left and not node.right and self.res.append(concat)
            node and (dfs(node.left, concat), dfs(node.right, concat))

        dfs(root)

        return self.res
