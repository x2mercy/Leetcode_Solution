    这道题真的。。很无语。。没有返回，只能在nums本身做修改
    要考虑两种情况，一种是k>len(nums)一种是k<len(nums)，解决这一矛盾的方法就是k%len(nums),如果k<len(nums)，则返回k，
    如果大于，返回余数
    还要注意[-k:]的意思是，从倒数第k（0开始）个元素到最后，[:-k]是从头到倒数第k个元素
