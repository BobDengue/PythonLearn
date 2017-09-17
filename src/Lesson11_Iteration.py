# #
# 迭代
# Iteration
# for...in...
# 的抽象程度非常高
# 可以迭代 list tuple 这种按照 index 存储的数据
# 也可以迭代 dict 这种按照 hash 存储的数据
# #

# # 低级迭代
# listExample = ['a','b','c','d']
# listIndex = list( range(4))
# for i in listIndex :
#     print(listExample[i])

# # 高级迭代
# listExample = ['a','b','c','d']
# for l in listExample :
#     print(l)

# # 对 dict的Key 迭代
# dictExample = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# for key in dictExample :
#     print(key)

# # 对 dict的Value 迭代
# dictExample = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# for value in dictExample.values() :
#     print(value)

# # 对 dict的Key和Value 同时迭代
# dictExample = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# for k,v in dictExample.items() :
#     print(k,v)
# 这里我们看到，for...in(): 可以对多变量进行迭代

# #
# 判断是否可迭代
# >>> from collections import Iterable

# >>> isinstance('abc',Iterable)
# True

# #
# 使用索引 
# enumerate()
# >>> L=[1,2,3,4,5,6,7,8,9]
# >>> list(enumerate(L))
# [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)]