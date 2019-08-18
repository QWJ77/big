# --------------------------没有参数，没有返回值----------------------------
# def test():
#     print(2**3)
#     print(2**4)
# test()

#----------------------------一个参数----------------------------------------
# 当我们需要动态地调整某个处理信息，就可以以参数的形式接手相关数据，num形参，3实参
# def test2(num):
#     print(num**3)
#     print(num**4)
# test2(3)

#------------------------------ 多个参数---------------------------------------
# 需要动态地调整多个处理信息
# 方式一：使用元组，元组不可变
# def 函数名（*arg）:

# def mySum(x,y):
#     print(x,y)
#     print(x+y)
# # mySum(3,5)
# mySum(y=1,x=3) #指明形参名称则不必严格按照顺序传参

# def mySum(t):
#     result=0
#     for v in t:
#         print(v)
#         result+=v
#     print(result)
# mySum((4,5,6,7))


# 不定长参数，在参数前加*，表示是个元组

# def mySum(*t):
#     print(t,type(t))
#     result=0
#     for v in t:
#         print(v)
#         result+=v
#     print(result)
# mySum(4,5,6,7)

#方式二：使用字典
# def 函数名（**dict）:
# 用关键字参数进行使用
# 函数名（参数名称1=参数1，参数名称2=参数2）

def mySum(**kwargs):
    print(kwargs,type(kwargs))
mySum(name="sz",age=12)
