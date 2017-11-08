    这道题要mark一下
    很有意思的算法，设了两个指针，一个快指针，一个慢指针，快指针每次.next.next，慢指针.next，用了try...except，如果是有cycle的话，
    慢指针和快指针总会遇到，于是返回true
    如果没有（except），返回false
