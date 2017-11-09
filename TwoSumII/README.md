    1. solution1中注释掉的解法是我原来的解法，但是对于很长的List报了time limit exceed的错误
    2. solution1中最终的做法需要mark！因为这种算法很常见，two pointers，一个从头，一个从尾，while l<r是不相遇的条件
      这种算法复杂度低，所以不会报time limit exceed
    3. solution2中用的是字典的算法（来自discuss），字典的key是numbers里的元素，value是index。每次循环只需要去查找字典内的key有没有
    等于target-num[i]的，如果有，直接返回value+1，如果没有，把num[i]也作为key存入字典。很机智
