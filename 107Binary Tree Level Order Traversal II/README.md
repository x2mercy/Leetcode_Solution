    1. collection.deque()：http://blog.csdn.net/qins_superlover/article/details/44338415
    deque()可以popleft()，移出第一个元素
    2. list[]，具体思路是把每一层的元素放在list[i]里，等于是多维数组，然后再reverse
    3. 要注意如果某一层有两个元素，则通过index>len(result)-1条件到else
