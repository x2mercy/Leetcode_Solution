    这道题一开始的思路是用二维数组做，可是没有成功，报错：list index out of range 之后会继续查相关资料研究一下
    后来看到大神的思路，是先用sorted（）将strs按照升序排列，然后将第一个元素赋给prefix，接下来把sort_strs里的
    元素与第一个元素（prefix）相比，如果不相同，则舍掉prefix最后一位再进行比较，直到相同，这里用了一个prefix[:-1]，
    作用是除了这个列表中的最后一个项目都保留，还有一个重点是s.startswith(str,beg=0,end=len(string)),beg和end
    可以省略，作用是检查字符串中是否以指定字符串开头。
