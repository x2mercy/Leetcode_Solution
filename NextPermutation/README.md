    讲真，这道题，我写完了都还不知道题目是什么意思（捂脸）
    算法是wikipedia上的：https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
    最后reverse list里的部分元素：nums[last_index+1:] = sorted(nums[last_index+1:])
    判断列表元素是否按照升序或降序排列：sorted(lst) == lst or sorted(lst, reverse=True) == lst
    https://www.cnblogs.com/clover-toeic/p/5600246.html
