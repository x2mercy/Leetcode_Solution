    这道题做的很快（solution1），因为上午刚做了reverse_int，所以很快就想到用reverse()，然后判断与x是否相等。
    但是看了提示发现里面说了要注意overflow的问题，可是。。我不知道哪里会overflow，因为如果x没有overflow，
    假如它是palindrome，那么它reversed之后应该也不会overflow，如果x不是palindrome，那么即使reversed之后
    overflow了，也判断为false。所以还不太清楚
    然后在github里找到了另外一个可行的解法
    https://github.com/RealHacker/leetcode-solutions/blob/master/009_palindrome_number/palindrome_number.py
    （solution2），不是偷懒用reverse做而是把比较左右两边的数字是否相同。
