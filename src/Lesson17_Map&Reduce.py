# #
# map
# 用法：
# map(function,Iterable)
# 作用：将 Iterable 带入 function函数，生成新的 Iterable 
# 例如：
# >>> def f(x):
# ...     return x * x
# ...
# >>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# >>> list(r)
# [1, 4, 9, 16, 25, 36, 49, 64, 81]
# #

# #
# reduce
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上
# 这个函数必须接收两个参数
# reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# #
# 但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
# >>> from functools import reduce
# >>> def fn(x, y):
# ...     return x * 10 + y
# ...
# >>> reduce(fn, [1, 3, 5, 7, 9])
# 13579
# #

# # str2int
# >>> from functools import reduce
# >>> def fn(x, y):
# ...     return x * 10 + y
# ...
# >>> def char2num(s):
# ...     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# ...
# >>> reduce(fn, map(char2num, '13579'))
# 13579

# # int2str
# from functools import reduce

# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#     def char2num(s):
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#     return reduce(fn, map(char2num, s))

练习：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
      如：输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：