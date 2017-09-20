class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1: 
            return l2
        if not l2:
            return l1
        if l1.val==l2.val:
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        if l1.val<l2.val:
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        if l1.val>l2.val:
            l2.next=self.mergeTwoLists(l2.next,l1)
            return l2
