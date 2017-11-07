# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        p=collections.deque()
        p.append((root,0))
        result=[]
        while p:
            node,index=p.popleft()
            if index>len(result)-1:
                result.append([node.val])
            else:
                result[index].append(node.val)
            if node.left:
                p.append((node.left,index+1))
            if node.right:
                p.append((node.right,index+1))
        result.reverse()
        return result        
                
                
                
                
        
        
