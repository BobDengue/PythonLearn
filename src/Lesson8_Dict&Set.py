# #
# 字典
# dict
# {}
# 字典是一种 Key-Value/Item 模型 ，通过 Key 来查询 Value 的值 ，Key不能相同，Value的值可以相同
# Key一定是一种 不可变对象 ，
# 
# dict 的建立
# dictExample = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# 
# dict 的访问
# 不存在Key则会报错
# dictExample['Bob']
# 
# dict 的查询（也就是查看是否 dict 中有这个Key）
# dictExample.get('Bob',-1)
# 如果有，就返回‘Bob’的 Value
# 如果没有，就返回 -1 ，也可以设定其他的返回值，如果省略的话，返回值为 none ，不会显示
# 或者
# in 方法，返回值为布尔型，False or True ，如
# 'Bob' in dictExample
# 返回 True
# 
# dict 的更改
# dict 的 Key 不可更改（只能删除），只能更改 Key 对应的 Value ,直接赋值就可以了
# dictExample['Tracy'] = 100
# 
# dict 增加 Key
# 直接赋值给新的Key，新的 Key 不能重复
# dictExample['Deng'] = 100
# 
# dict 删除 Key 和对应的 Item
# dictExample.pop( 'Deng'[,100])
# 返回值 100
# [,100] 可以省略，返回值是 Key 对应的 Item
# #

# #
# 集合
# set
# 一系列 不重复 且 无序 的元素集合
# 与 dict 类似，但是只存储 Key ，不存储 Item/Value
# 定义 ： set() 方法
# setExample = set([1,2,3])
# 可以定义一个空的 set ，也可以用 list 来定义/新建一个 set
# 
# 增加元素 
# 增加的元素没有顺序，因为本身也是无序的
# setExample.add(4)
# 
# 删除元素
# setExample.delete(4)
# 
# 因为 set 可以看成数学上的集合，所以还会有集合的操作
# 
# 交集 s and s1
# 
# 并集 s or s1
# #