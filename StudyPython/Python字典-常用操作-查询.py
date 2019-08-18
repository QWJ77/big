# 获取单个值
# 方式一
# dic[key]
# 如果key不存在则报错
# d={"name":"sz","age":"18"}
# print(d["age"])

# 方式二
# dic.get(key[,default])
'''
如果不存在对应的key,则取给定的默认值default
如果没有默认值，则为None
但不会报错
但是，原字典不会新增这个键值对
dic.pop(key[,default])弹出指定的对，并返回对应的值
'''
# d={"name":"sz","age":"18"}
# v=d.get("age1",666)
# print(v)

# 方式三
'''
dic.setdefault(key[,default])
获取指定key对应的值
如果key不存在，则设置给定的默认值并返回该值
如果没有默认值，则为None
原字典会增加这个键值对！！！
'''
d={"name":"sz","age":"18"}
# v=d.setdefault("age1")
# print(v,d)

#以下几种方式获取到的结果都是Dictionary view object，不是字典,不能通过下标获取,字典变化时，它也发生变化
# 获取所有的键
# dic.keys()
# k=d.keys()
# print(k)
# print(list(k))

# 获取所有的值
# dic.keys()
# print(d.values())

# 获取字典的键值对
# dic.items()
i=d.items()
print(i)
