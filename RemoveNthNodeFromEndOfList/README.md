    用了快慢指针的算法！
    但是只用两个指针是不够的，还需要有个prev，来指向原来的slow，这样当slow指向需要被remove的节点时，prev可以直接直接指向slow.next,
    然后slow.next指向none
    还要考虑一种情况：slow还没开始移动就已经结束循环了，即：当n等于链表长度时，fast在while之前就是none了，这样的情况下，prev是none，
    此时应保留head.next之后的所有节点，则head=head.next即可
