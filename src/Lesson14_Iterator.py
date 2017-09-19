# #
# 迭代器
# Iterator
# 迭代器对象 ：
# 可以被 next() 方法（和 for...in 方法）访问
# # 这里的 for...in 方法表示多次调用 next() 方法
# 通常就是 生成器对象
# 迭代器对象不断调用，然后返回下一次的值，直到抛出 StopIteration 错误
# 迭代器对象是惰性的，只能一步一步的调用，而不能用 len() 之类的方法访问
# 也就是说迭代器对象：只知道 迭代器的当前值 和 迭代方法 
# 这样就可以用 初值+方法 来表示无限的序列（如：整数序列）
# #
# 判断是否为 迭代器对象
# >>> from collections import Iterator
# >>> isinstance((x for x in range(10)), Iterator)
# True
# >>> isinstance([], Iterator)
# False

# #
# 可迭代
# Iterable
# 可迭代对象：
# 可以使用 for...in 方法 的对象都成为可迭代对象
# 可迭代对象 包含 迭代器对象 和 非迭代器对象 两部分
# 非迭代器对象包括：
# list
# tuple
# dict
# set
# str
# 他们都是已经确定的对象
# 存储方式是：所有值 
# #
# 判断是否为可迭代对象
# >>> from collections import Iterable
# >>> isinstance([], Iterable)
# True

# #
# transfer Iterable to Iterator
# 使用 iter() 方法
# #
# >>> L = [1,2,3]
# >>> from collections import Iterable
# >>> isinstance(L,Iterable)
# True
# >>> from collections import Iterator
# >>> isinstance(L,Iterator)
# False
# >>> isinstance(iter(L),Iterator)
# True