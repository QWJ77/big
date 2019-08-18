# 无序的！！！不可随机访问的！！！不可重复的元素集合！！！
# str="abc"  #有序
# l=[1,2,3]   #有序
# t=(1,2,3)   #有序
# d={"name":"sz","age":18}   #无序，不能通过索引获取
# s={1,2,3}
'''
可变集合
'''
# 方式一
# s={1,2,3}
# print(s,type(s))
# 方式二
# sz=set("abc")
# s1=set([1,2,3])
# s2=set((1,2,3))
# s3=set({"name":"sz","age":18})#接收对象是字典的时候，会生成key的集合对象
# print(sz,s1,s2,s3)
# 方式三，推导式
# s=set(x for x in range(0,10))
# s={x for x in range(0,10)}
# print(s,type(s))

'''
不可变集合，不能使用s{}
'''
# fs=frozenset("abc")
# fs=frozenset([1,2,3])
# fs=frozenset((1,2,3))
fs=frozenset({"name":"sz","age":18})
print(fs,type(fs))

# 推导式
s = frozenset(x**2 for x in range(0, 10) if x%2==0)
print(s)

# 创建一个空集合时，需要使用set()或者frozenset(),不能使用s{},会被识别为字典
# 集合中的元素，必须是可哈希的值（列表和字典是可变的，是不可哈希的）
# 如果集合中的元素值出现重复，则会被合并为1个


# 可用于列表去重
l=[1,2,3,3,3]
s=set(l)
print(s)
result=list(s)
print(result,type(result))
