# #
# 列表
# List
# 用 [] 来定义列表
# 其中的元素可以不同，接近于一个数组，如 
# num = [1,2,3] 
# chr = ['A','B','C'] 
# ls = [1,'A',[1,'A']]
# 元素的访问
# 正序
# num[0]  
# 逆序
# ls[-1]
# 列表的长度用 len() 来访问
# #

# #
# List的操作
# 
# listExample = ['A','B','C','D','E','F','G','H','I','J']
# 
# append 方法，在尾部增加一个元素()
# listExample.append('A')
# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'A']
# 
# insert 方法，在序号位置插入元素，其余元素自动后移
# listExample.insert(2,'A')
# ['A', 'B', 'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'A']
# 
# pop 方法，弹栈，从尾部删除一个元素
# listExample.pop()
# ['A', 'B', 'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# 或者，从序号位置删除，序号后元素自动前移
# listExample.pop(2)
# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# 
# 修改 list 元素
# 直接对 list 元素幅值，两个元素的值的类型可以不一样
# listExample[0] = ['A',1]
# [['A', 1], 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# listExample[0][0] = 1
# [[1, 1], 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# #

# #
# 元组
# Tuple
# 用 （） 来定义
# Tuple 和 List 很类似，但是 Tuple 确定后，其元素指针不可更改，没有 List 的各种方法
# tupleExample = (1,'A')
# 一元元组的定义
# 由于 () 会造成歧义，所以一元元组的定义如下
# newTupleExample = (1,) 
# 一种可变的元组设计，把list当成元组的元素，通过修改list来达到修改tuple的目的，如
# newTupleExample1 = (1,2,[1,2])
# newList = [1,2,3]
# newTupleExample1[2][0] = newList
# (1, 2, [[1, 2, 3], 2])
# #

# #
# 练习：请用索引取出下面list的指定元素：
# #
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])