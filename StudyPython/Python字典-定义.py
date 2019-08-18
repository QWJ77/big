# 无序的，可变的键值对集合
'''
方式一{key1:value1,key2:value2,...}

'''
# person={"name":"sz","age":18}
# # 注：不能通过索引去取
# print(person["name"])
# print(person["age"])

'''
方式二
静态方法，生成字典类和对象都可以进行调用
dict.fromkeys(seq,value=None),一般不用对象去调用，seq可以是字符串，列表，元祖等序列
'''
# d=dict.fromkeys("abc") #{'a': None, 'b': None, 'c': None}
# print(d)
# f=dict.fromkeys("abc",666)
# print(f)


'''
字典的key不能重复!!!!
'''
# d={1:"a",2:"b",1:"c"}
# print(d)#如果key重复，最后只留下一个，后面的会把前面的覆盖掉
'''
字典的key必须是任意不可变的类型
'''
# d={[1,2,3]:"123"} 错误，列表不是不可变类型
# num1=10
# print(id(num1))
# num2=20
# print(id(num2))
# # 值不一样，内存地址也不一样

# l=[1,2,3]
# print(l,id(l))
# l.append(4) #append会直接改变列表本身
# print(l,id(l))
# 列表变了但是内存空间不变

'''
原理：
把key通过“哈希函数”转换成一个整型数字，成为“哈希值”
讲该数字对数组长度进行取余，取余结果就当做数组的下标
如果产生了“哈希冲突”，比如计算出的索引是同一个，则采用开发寻址法，通过探测函数查找下一个空位
存在意义：
1、可以通过key访问，使得这种访问更具备意义
2、查找效率得到很大的提升
'''

