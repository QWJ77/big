'''
单一集合操作
可变集合：增删查
不可变集合：查
'''
#----------------------------------可变集合-------------------------------------

#新增
#通过一个对象方法add(),必须是可哈希的值
# s={1,2,3}
# s.add(4)
# print(s,type(s))
#删除操作
# s.remove(element),如果删除的元素不存在，则报错KeyError
# result=s.remove(13)
# print(result,s)

# s.discard(element)
# 若没有这个元素，则do nothing,什么都不做
# result=s.discard(13)
# print(result,s)

# s.pop(element)
# 随机删除并返回集合中的元素
# 若集合为空,则返回一个错误
# result=s.pop()
# print(result,s)

# s.clear()
# 情况一个集合的所有元素
#
# result=s.clear()
# print(result,s)

# del删除整个变量


# 查
s={1,2,3}
# for v in s:
#     print(v)

#用迭代器方法
# 1、生成迭代器
its=iter(s)
# 2、使用这个迭代器生访问
# print(next(its))
# print(next(its))
# print(next(its))

for v in its:
    print(v)
# ----------------------------------不可变集合-------------------------------------

# 查
s=frozenset([1,2,3])
for v in s:
    print(v)

#用迭代器方法
# 1、生成迭代器
its=iter(s)
# 2、使用这个迭代器生访问
# print(next(its))
# print(next(its))
# print(next(its))

for v in its:
    print(v)