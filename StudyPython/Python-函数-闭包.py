'''
在函数嵌套的前提下
内层函数引用了外层函数的变量（包括参数）
外层函数又把内层函数当做返回值返回
这个内层函数+所引用的外层变量，称为闭包
'''

# def test():
#     a=10
#     def test2():
#         print(a)
#     return test2
#
# newFunc=test()
# newFunc()


# def line_config(content,length):
#     def line():
#         print("--"*(length//2)+content+"--"*(length//2))
#     return line
# line1=line_config("闭包",20)
# line1()
'''
1、闭包中，如果需要修改外层引用的变量，需要使用nonlocal变量声明
否则会当做闭包内新定义的变量！！
'''
# def test():
#     num=10
#     def test2():
#         nonlocal num
#         num=666
#         print(num)
#     print(num)
#     test2()
#     print(num)
#     return test2
# result=test()


'''
2、当闭包内引用了后期会发生变化的变量时，一定要注意
'''
# def test():
#     a=1
#     def test2():
#         print(a)
#     a=2
#     return test2
# newFunc=test()  #此时test2并没有被执行
# newFunc()

# 函数什么时候才会确定内部变量标识对应的值？
# 当函数被调用的时候，才会真正确定对应的值到底是什么，在此之前都是普通的变量标识
# def test():
#     print(b)
# print("xxxx")
#
# test()

# def test():
#     func=[]
#     for i in range(1,4):  #每一次循环，内部都定义一个新函数
#         def test2():
#             print(i)
#         func.append(test2)#列表里是3个函数
#     return func
# newFunc=test()
# print(newFunc)
# newFunc[0]()
# newFunc[1]()
# newFunc[2]()

def test():
    func=[]
    for i in range(1,4):  #每一次循环，内部都定义一个新函数
        def test2(num):
            def inner():
                print(num)
            return inner
        func.append(test2(i))#列表里是3个函数，三个inner
    return func
newFunc=test()
print(newFunc)
newFunc[0]()  #拿的是inner（）
newFunc[1]()
newFunc[2]()