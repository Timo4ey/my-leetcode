# Given a binary tree root and an integer target, delete all the leaf nodes with value target.

# Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).

# Example 1:

# Input: root = [1,2,3,2,null,2,4], target = 2
# Output: [1,null,3,null,4]
# Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left).
# After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).
# Example 2:

# Input: root = [1,3,3,3,2], target = 3
# Output: [1,3,null,null,2]
# Example 3:

# ￼

# Input: root = [1,2,null,2,null,2], target = 2
# Output: [1]
# Explanation: Leaf nodes in green with value (target = 2) are removed at each step.

# Constraints:

# The number of nodes in the tree is in the range [1, 3000].
# 1 <= Node.val, target <= 1000


# ---------------------------------------Runtime 42 ms Beats 78.43% Memory 16.96 MB Beats 98.37%---------------------------------------


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def is_node_val(self, node: Optional[TreeNode], target: int):
        if node:
            if node.val == target and node.left is None and node.right is None:
                return None
            return node

    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:

        def dfs(node: Optional[TreeNode]):
            if node:
                node.left = dfs(node.left)
                node.right = dfs(node.right)
                node.left = self.is_node_val(node.left, target)
                node.right = self.is_node_val(node.right, target)
                node = self.is_node_val(node, target)
                return node

        return dfs(root)
