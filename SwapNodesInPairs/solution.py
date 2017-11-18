# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev,prev.next=self,head
        while prev.next and prev.next.next:
            current=prev.next
            next_node=current.next
            prev.next,next_node.next,current.next=next_node,current,next_node.next
#            prev.next=next_node
#            next_node.next=current
#            current.next=next_node.next            
            prev=current
        return self.next
            
