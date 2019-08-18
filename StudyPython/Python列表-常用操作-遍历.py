#--------------------------方式一----------------------------
# 根据元素进行遍历
# 并打印出索引
# values=["a","b","c","a","d"]
# currentIndex=0
# for v in values:
#     print(v)
#     print(values.index(v,currentIndex))
#     currentIndex+=1

# -------------------------方式二-------------------------
# 根据索引进行遍历
# values=["a","b","c","a","d"]
# 造一个索引列表，就是我们要遍历的索引列表 0-4,当索引多时用列表生成式
# # indexs=[0,1,2,3,4]
# # indexs=range(5) #动态修改麻烦
# count=len(values)
# indexs=range(len(values))
# 遍历整个索引列表，遍历的同时获取每一个索引，根据索引值获取到指定元素
# for index in indexs:
#     print(index,values[index])

#--------------------------方式三--------------------------------------
# 语法enumerate（sequence，[start=0]） start表示让索引从几开始，默认索引从0开始
values=["a","b","c","a","d"]
# 先根据列表创建一个枚举对象
print(list(enumerate(values)))
# 结果：[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'a'), (4, 'd')]
# 遍历整个枚举对象（枚举变量可以直接被遍历）
# for tuplevalue in enumerate(values):
#     # print(tuple)
#     print(tuplevalue[0])
#     print(tuplevalue[1])
# for tuplevalue in enumerate(values):
#     idx,val=tuplevalue #直接分解了每个元组的值
#     print(idx)
#     print(val)
#   idx,val=[0,"a"]
for idx,val in enumerate(values,1):
    print(idx)
    print(val)




