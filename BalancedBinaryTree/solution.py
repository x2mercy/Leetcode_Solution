# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        DL=self.depth(root.left)
        DR=self.depth(root.right)
        
        if DL-DR<-1 or DL-DR>1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    def depth(self,node):
        if node==None:
            return 0
        DL=self.depth(node.left)
        DR=self.depth(node.right)
        return max(DL,DR)+1
        
