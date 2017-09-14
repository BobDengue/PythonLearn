# #
# 字典
# dict
# {}
# 字典是一种 Key-Value/Item 模型 ，通过 Key 来查询 Value 的值 ，Key不能相同，Value的值可以相同
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
