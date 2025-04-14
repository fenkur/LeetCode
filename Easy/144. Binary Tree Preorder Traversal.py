# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def preorder(root, result):
            if root != None:
                result.append(root.val)
                preorder(root.left, result)
                preorder(root.right, result)
        result = []
        preorder(root, result)
        return result
        