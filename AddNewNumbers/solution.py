# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur1=l1
        adder1=0
        i=0
        while cur1:
            adder1+=cur1.val*(10**i)
            cur1=cur1.next
            i+=1
        cur2=l2
        adder2=0
        j=0
        while cur2:
            adder2+=cur2.val*(10**j)
            cur2=cur2.next
            j+=1
        add=adder1+adder2
        root=n=ListNode(0)
        
        digit=add%10
        add=add/10
        while add>0:
            
            n.next=ListNode(digit)
            n=n.next
            digit=add%10
            add=add/10
        n.next=ListNode(digit)
        return root.next
            
