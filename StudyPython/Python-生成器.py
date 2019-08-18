'''
生成器：是一个特殊的迭代器
所有迭代器的特性：
1、惰性计算数据，节省内存
2、能够记录状态，并通过next（）函数，访问下一个状态
3、具备可迭代特性
但是要自己打造一个迭代器比较复杂，所以用一种更优雅的方式“生成器”
'''
#1、 生成器的创建方式1：将列表生成式的[]改成()
# l=[i for i in range(1,100) if i%2==0]
# print(l)#很浪费内存
# l=(i for i in range(1,1000) if i%2==0)
# #访问生成器的方法
# print(next(l))
# print(next(l))
# print(l.__next__())

# 2、生成器的创建方式2:yield语句，生成结果就是个生成器
# yield可以阻断当前函数的执行，当使用next()或者__next__(),都会让函数继续执行，
# 当执行下到一个yield的时候，又会被暂停，并记录当前的状态返回给外界（1，2，3，4），
#
# def test():
#     yield 1
#     print("a")
#
#     yield 2
#     print(2)
#
#     yield 3
#     print("b")
#
#     yield 4
#     print("c")
#
#     yield 5
#     print("d")
def test():
    for i in range(1,9):
        yield i
g=test()    #仅仅是为了产生一个生成器，没有其他作用,
print(g)
print(next(g))
print(next(g))


