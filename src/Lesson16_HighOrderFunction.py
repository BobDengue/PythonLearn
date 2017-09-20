# #
# 变量可以指向函数
# 例如：
# f = abs 
# 之后 f() 就指向 abs() 函数
# 也就是 f 成了 abs 的别名
# #

# #
# 函数名也可以指向变量
# abs = 10 
# 之后 abs 就指向 10 这个值
# 不指向 绝对值函数了，也就没了绝对值的功能
# 要恢复只能重启 python 环境
# #

# #
# 高阶编程
# 把 函数 作为参数 传入另一个函数
# 例如：方均根函数 RMS
# #

import math
from Lesson16_HighOrderFunction_RMS import RMS
listExample = list( range(10))
print( listExample)
print( RMS( math.sqrt ,*listExample ))
