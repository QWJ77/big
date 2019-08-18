# 删
# 1、del
# key必须要存在，如果删除的key不存在，则报错keyError
# d={"name":"sz","age":"18"}
# del d["age"]
# print(d)

# 2、dic.pop(key[,default])弹出指定的对，并返回对应的值
# 如果key不存在，则返回给定的default值，不做删除动作
# 如果没有指定默认值，则报错
# v=d.pop("age")
# print(v)

# dic.popitem()
# 删除按照升序排列的第一个键值对，并以“元组”的形式返回该键值对
# 如果字典为空，则报错
# d={"name":"sz","zage":"18","a":123}
# result=d.popitem()
# print(result,d)  #('a', 123) {'name': 'sz', 'zage': '18'}

# dic.clear()
# 删除字典内所有键值对
# 注：字典对象本身还存在。只不过内容被清空
# del会删除地点对象
d={"name":"sz","zage":"18","a":123}
print(d.clear())
print(d)