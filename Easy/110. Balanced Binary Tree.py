# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check(node):
            if not node:
                return 0  # Base case: height of empty subtree is 0
            left_height = check(node.left)
            if left_height == -1:
                return -1  # Left subtree is unbalanced
            right_height = check(node.right)
            if right_height == -1:
                return -1  # Right subtree is unbalanced
            if abs(left_height - right_height) > 1:
                return -1  # Current node is unbalanced
            return max(left_height, right_height) + 1  # Return height
        return check(root) != -1