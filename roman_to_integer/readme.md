    这道题也是easy程度的，渐渐适应了用Python做题，也习惯了去搜一些python的语法。
    首先，这道题用了dictionary的类型来存储数据，dictionary类型的特征是存储了key和value，可以通过key的值来找到对应的value。
    比如这道题中，把罗马字母存为key，对应的integer存为value，就可以很容易的解决了。
    这道题一开始错误是在，用dictionary存储integer的时候把integer当成string存储了，导致报错，因为string不能加减。
    这道题的核心除了用dictionary存储之外，还有就是通过比较current罗马字母和next罗马字母来判断是加还是减。
