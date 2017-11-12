    第一次写的可快了，例子也全部跑通，可是time limit exceed
    因为我用了两层循环，可能比较慢
    后来用了left和right指针，这种算法真的很常见，要Mark一下
    left+1和right-1的条件分别是：如果height[left]和height[right]哪个小，left小就+1，right小就-1
