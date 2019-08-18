'''
值传递：传递过来的是一个数据的副本，修改副本对原件没有任何影响
引用传递：传递过来的是一个变量的地址，通过地址可以操作同一份文件
注：在Python中，只有引用传递
但是，如果数据类型是可变类型，则可以改变原件
如果数据类型是不可变类型，则不可以改变原件
可变数据类型：列表list和字典dict；
不可变数据类型：整型int、浮点型float、字符串型string和元组tuple。
'''

# 如果数据类型是不可变类型，则不可以改变原件
# def change(num):
#     print(id(num))
#     num=666
#     print(id(num))
#
# b=10
# print(id(b))  #b和num id相同，说明b把它所指内存的唯一表示传给了num
# change(b)
# print(b)

# 如果数据类型是可变类型，则可以改变原件

def change(num):
    print(id(num))
    num.append(666)
    print(id(num))


b=[1,2,3]
print(id(b))
change(b)
print(b)