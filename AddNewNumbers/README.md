 My first medium level problem.
 The only thing that need to be paid attention to is how to create a new linked list and return it.
   root=n=ListNode(0)//initialize
            n.next=ListNode(digit)//give value
            n=n.next
            digit=add%10
            add=add/10
        n.next=ListNode(digit)
        return root.next//return
