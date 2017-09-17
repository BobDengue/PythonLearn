#
切片
slice
从
list ['a','b','c','d']
tuple (1,2,3,4)
string 'ABDC'
中截取一部分
#

# #
# 使用方法
# list[start:end:interval]
# 从序号 start 取到 end ，且不算 end
# 每隔 interval 取一个
# list 的编号
# listExample = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]
# index           0   1   2   3   4   5   6   7   8
# indexReverse    -9  -8  -7  -6  -5  -4  -3  -2  -1
# 如果序号中出现 0 和 -1 ，则可以省略
# 同时 切片一定要按照顺序 切片
# 也就是只能从左到右切片
# 正序：[n1:n2] n1<n2 如
# >>> listExample = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]
# >>> listExample[1:5]
# [2, 3, 4, 5]
# >>> listExample[2:0]
# []
# 逆序：[n1:n2] n1<n2
# >>> listExample[-3:-1]
# [7, 8]
# >>> listExample[-3:-5]
# []
# #