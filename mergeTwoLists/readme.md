    这道题用了两种方法：recursively和iterator。
    recursively比较难理解，画出stack模型会比较容易理解，主要是通过反复调用方法来实现。
    iterator比较容易理解，主要思想是创造两个新的链表，result和current，current负责存储通过比较l1和l2得出的结果的节点，
    result负责最后的返回，result=current=ListNode(0)。要注意：每次比较完之后，要用l1=l1.next来移动到下一个节点进行比较
    同时，每一次循环最后都需要current=current.next来移动到下一个节点。当l1或者l2的节点为none时，跳出循环，使用current.next=l1orl2
    来将另外一个节点剩余节点存入current，最后return result.next
