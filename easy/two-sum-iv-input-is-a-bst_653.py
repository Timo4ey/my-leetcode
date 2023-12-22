# Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

# Example 1:

# ￼
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
# Example 2:

# ￼
# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false


# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -104 <= Node.val <= 104
# root is guaranteed to be a valid binary search tree.
# -105 <= k <= 105

# ---------------------------------------Runtime 94 ms Beats 14.66% Memory 19.5 MB Beats 75.52%---------------------------------------


from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = []

        def dfs(node):
            if node:
                nums.append(node.val)
                dfs(node.left)
                dfs(node.right)

        def binSearch(array: list[int], target):
            start, end = 0, n - 2

            while start <= end:
                mid = (start + end) // 2
                guess = array[mid]
                if guess == target:
                    return True
                if guess > target:
                    end = mid - 1
                elif guess < target:
                    start = mid + 1
            return False

        dfs(root)
        nums.sort()
        n = len(nums)

        res = False
        nums = deque(nums)
        i = 0
        while i < n:
            num = nums.pop()
            target = k - num
            res = binSearch(nums, target)
            if res:
                return True
            i += 1
            nums.appendleft(num)
        return False
