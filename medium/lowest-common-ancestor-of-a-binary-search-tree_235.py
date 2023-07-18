# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia:
# “The lowest common ancestor is defined between two nodes p and q
# as the lowest node in T that has both p and q as descendants
# (where we allow a node to be a descendant of itself).”


# Example 1:

# ￼
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:

# ￼
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [2,1], p = 2, q = 1
# Output: 2
# ---------------------------------------Runtime 92 ms Beats 67.3% Memory 20.8 MB Beats 56.47%---------------------------------------


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def is_greater_than_node(node):
            return (
                True
                if node and node.val > p.val and root.val > q.val
                else False
            )

        def is_less_than_node(node):
            return (
                True
                if node and node.val < p.val and root.val < q.val
                else False
            )

        while True:
            if is_greater_than_node(root):
                root = root.left
            elif is_less_than_node(root):
                root = root.right
            else:
                return root
