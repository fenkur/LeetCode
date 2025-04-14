# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def postorder(root, result):
            if root != None:
                postorder(root.left, result)
                postorder(root.right, result)
                result.append(root.val)
        result = []
        postorder(root, result)
        return result
        