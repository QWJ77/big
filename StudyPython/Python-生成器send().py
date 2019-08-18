# send会启动上一次挂起的程序，并给上一次挂起的程序一个返回值
# 注：第一次调用，t.send(None)
def test():
    print("xxx")#并不会执行，只有在调用test()方法的时候才会启动
    res1=yield 1 #"ooo"
    print(res1)
    res2=yield 2
    print(res2)

g=test() #g就是一个生成器
print(g.__next__()) #只有调用next()函数时，才启动调用test函数
# print(g.__next__())
print(g.send("ooo"))