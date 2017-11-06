# this solution is Time Limit Exceeded
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        result1=[]
        result1.append(p.val)
        while p:
            if p.left!=None:
                result1.append(p.left)
            if p.right!=None:
                result1.append(p.right)
        result2=[]
        result2.append(q.val)
        while q:
            if q.left!=None:
                result1.append(q.left)
            if q.right!=None:
                result1.append(q.right)
        result=cmp(result1,result2)
        if result==0:
            return True
        else:
            return False
        
