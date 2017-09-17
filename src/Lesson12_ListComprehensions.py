# #
# 列表生成器
# list(range())
# list(for...in)
# list() 其实是循环的简便写法，所以循环能干的大部分，列表生成器都可以干
# #

# 直接生成
# >>> list(range(1, 11))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # 一层循环
# >>> list(x*x for x in range(1,10))
# [1, 4, 9, 16, 25, 36, 49, 64, 81]
# <=>
# >>> L = []
# >>> for x in range(1, 11):
#         L.append(x * x)
# >>> L
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# # 两层循环
# >>> list(x*x for x in range(1,10) if x%2 == 0)
# [4, 16, 36, 64]

# # 列出文件名
# import os # 导入os模块，模块的概念后面讲到
# print( [d for d in os.listdir('.')]) # os.listdir可以列出文件和目录

# 练习：如果list中既包含字符串，又包含整数，
# 由于非字符串类型没有lower()方法，所以列表生成式会报错
# L1 = ['Hello', 'World', 18, 'Apple', None]
# 期待输出: ['hello', 'world', 'apple']
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = list(l for l in L1 if( isinstance(l,str)) )
print(L2)