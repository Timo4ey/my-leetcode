# Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

# Example 1:

# ￼
# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
# Example 2:

# ￼
# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]


# Constraints:

# The number of nodes in each tree is in the range [0, 5000].
# -105 <= Node.val <= 105

# ---------------------------------------Runtime 179 ms Beats 66.23% Memory 20.25 MB Beats 83.02%---------------------------------------

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.store = []

        def dfs(node: TreeNode) -> TreeNode:
            if node:
                self.store.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root1)
        dfs(root2)
        self.store.sort()
        return self.store
