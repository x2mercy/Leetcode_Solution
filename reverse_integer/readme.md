    Reverse digits of an integer.

    Example1: x = 123, return 321
    Example2: x = -123, return -321

    click to show spoilers.

    Note:
    The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
    
    这道题我本来的思路是用不断除以10的方式，直到/10=0，然后把余数存放到数组中的方式，但是后来发现还有一种更简便的方法，用reversed()函数，可以直接
    颠倒string的内容，所以就是先把x转换成string，再进行reversed()。
    
    还要注意32bit signed int最大值为2^31-1，最小值为-2^31
    
    'sep'.join(seq)，可以返回一个以分隔符sep连接各个元素后生成的字符串。
