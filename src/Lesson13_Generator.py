# # 
# 生成器
# 如果列表元素可以按照某种算法推算出来，
# 那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。
# 在Python中，这种一边循环一边计算的机制，
# 称为生成器：generator。
# #

# #
# 创建方法一
# 一是吧创建 list 的 [] 改成 () ,例如
# # list [ x表达式 for迭代 条件 ]
# >>> listExample = [ x for x in range(10) if x%2==1]
# >>> listExample
# [1, 3, 5, 7, 9]
# # generator ( x表达式 for迭代 条件 )
# >>> generatorExample = ( x for x in range(10) if x%2==1)
# >>> generatorExample
# <generator object <genexpr> at 0x0403CE10>
# >>> next(generatorExample)
# 1
# >>> next(generatorExample)
# 3
# >>> next(generatorExample)
# 5
# >>> next(generatorExample)
# 7
# >>> next(generatorExample)
# 9
# >>> next(generatorExample)
# Traceback (most recent call last):
#   File "<pyshell#23>", line 1, in <module>
#     next(generatorExample)
# StopIteration
# 生成器 generator 的访问最基本的是 next()
# next() 是计算当前值的下一个值，也就是说生成器 generator 会记录并返回到记录的那个值
# 并且重新调用原来的方法
# 也可以用 for...in 来访问 generator ，其实也是调用的 next() 方法，例如：

# >>> for xValue in generatorExample :
# 	print( xValue)

	
# >>> 
# # 如果在上面的基础上使用 for...in 访问，结果并不会出现print的结果
# # 原因是 生成器 会记录返回值的位置
# # 上面已经出现了 StopIteration ，也就是迭代结束，generator不能继续迭代
# # 所以没有返回值，不能print
# # 重新对 generatorExample 赋值，就可以对生成器进行检索
# >>> generatorExample = ( x for x in range(10) if x%2==1)
# >>> for xValue in generatorExample :
# 	print( xValue)

	
# 1
# 3
# 5
# 7
# 9

# #
# 创建方法二
# yield 方法 
# 注意 函数（function） 与 生成器（generator） 的差异
# function 在 return 之后 ，不记录 return 的位置，重新迭代
# generator 在 yield 之后，记录 yield 的位置，再次调用 next() 方法时，从 yield 位置开始迭代
# function 返回结果（值）
# generator 返回一个 generator 对象
# 以 斐波拉契数列 为例
# # function
# # 打印出 fib 的列表list
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b # 这里相当于组成了一个 tuple
#         n = n + 1
#     return 'done'
# # generator
# # 生成 generator
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b # 这里相当于组成了一个 tuple
#         n = n + 1
#     return 'done'
# #
# fibExample = fib (5)
# # 一般访问 generator 需要重新新建一个对象，避免反复第一次调用 如：
# >>> def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b # 这里相当于组成了一个 tuple
#         n = n + 1
#     return 'done'

# >>> fib(5)
# <generator object fib at 0x04041B40>
# >>> next(fib(5))
# 1
# >>> next(fib(5))
# 1
# >>> next(fib(5))
# 1
# >>> next(fib(5))
# 1
# >>> f = fib(5)
# >>> next(f)
# 1
# >>> next(f)
# 1
# >>> next(f)
# 2
# >>> next(f)
# 3
# >>> 

# 作业：输出杨辉三角
#           1
#         1   1
#       1   2   1
#     1   3   3   1
#   1   4   6   4   1
# 1   5   10  10  5   1

from Lesson13_Generator_Triangles import Triangles
trianglesExample = Triangles()
for n in range(10) :
  print( next(trianglesExample))

# PS D:\Documents\PythonLearn\src> py .\Lesson13_Generator.py
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]