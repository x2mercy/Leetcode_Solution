    妈的这道题太特么气人了 题目也没说找出的所有list必须按照原List的排列顺序排
    solution1.py出来的结果过不了checker，但我觉得，只要返回所有相加为0的三个元素list就ok
    solution2.py是用two pointer做的，先sort，主要是有一个i一直+1，然后l=i+1，r=len(nums)-1，从两边加减
    然后相加如果小于0，则l+1，如果大于0，r-1
    需要注意的是！要避免重复！在循环的开始，要比较nums[i]和nums[i-1]的大小，如果是一样的，就要continue,不然会重复
    在循环的最后，要看一下nums[l]是否等于nums[l+1]以及nums[r]是否等于nums[r+1]，因为如果相等的话，再进行l+1和r+1的操作
    又会重复
