# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        DL=self.minDepth(root.left)
        DR=self.minDepth(root.right)
        d=min(DL,DR)
        D=max(DL,DR)
        if DL==0 or DR==0:
            return D+1
        else:
            return d+1
        
