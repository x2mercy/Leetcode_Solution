    本来想从第一个元素开始，挨个比较，然后用del操作删掉重复的元素，但是定义nums[i+1]会报错:list index out of range，
    题目又说不可以allocate另外一个列表来做，所以定义j来作为中间值，如果num[i]!=num[j]，则j+1，将num[i]的值赋给num[j]，
    如果相等，则继续i+1比较下一个元素，这样最后将j+1就是len
