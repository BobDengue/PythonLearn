# # 
# 生成器
# 如果列表元素可以按照某种算法推算出来，
# 那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。
# 在Python中，这种一边循环一边计算的机制，
# 称为生成器：generator。
# #

#
创建方法
一是吧创建 list 的 [] 改成 () ,例如
# list [ x表达式 for迭代 条件 ]
>>> listExample = [ x for x in range(10) if x%2==1]
>>> listExample
[1, 3, 5, 7, 9]
# generator ( x表达式 for迭代 条件 )
>>> generatorExample = ( x for x in range(10) if x%2==1)
>>> generatorExample
<generator object <genexpr> at 0x0403CE10>
>>> next(generatorExample)
1
>>> next(generatorExample)
3
>>> next(generatorExample)
5
>>> next(generatorExample)
7
>>> next(generatorExample)
9
>>> next(generatorExample)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    next(generatorExample)
StopIteration
生成器 generator 的访问最基本的是 next()
next() 是计算当前值的下一个值
