class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        count = r = l = 0
        count = 1
        def walk(tree, position):
            nonlocal count
            if position == 'left' and tree.right:
                count += 1
                return walk(tree.right, 'right')
            if position == 'right' and tree.left:
                count += 1
                return walk(tree.left, 'left')
            return count
        if root.left and root.right:
            r = walk(root.right, 'right')
            l =  walk(root.left, 'left')
        elif root.left:
            l =  walk(root.left, 'left')
        elif root.right:
            r = walk(root.right, 'right')
        return max(r, l)