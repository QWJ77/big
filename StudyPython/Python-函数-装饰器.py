'''
在函数名函数体不改变的情况下，给一个函数额外附件一写代码
'''
# 定义两个功能函数
# def checkLogin(func):
#     def inner():
#         print("登录验证...")
#         func()
#     return inner
# @checkLogin
# def fss():
#     print("发说说")
# @checkLogin
# def ftp():
#     print("发图片")

# fss=checkLogin(fss)
# ftp=checkLogin(ftp)

#相关业务逻辑代码
# btnIndex =1
# if btnIndex ==1:
#     # print("登录验证...")
#     fss()
# else:
#     print("登录验证...")
#     ftp()
#功能函数不变，而业务代码很多，直接在业务逻辑代码里修改，就造成每一份逻辑代码在调用具体功能函数之前
# ，去登录严重都需要，代码冗余度大，复用性比较差，维护比较难

'''
装饰器
作用：在函数名以及函数体不变的前提下，给一个函数附加一些额外代码
语法糖：@
装饰器执行时间是立即执行
装饰器的叠加：从上到下装饰，从下到上执行

'''
# 想给发说说函数增加一些额外功能，
# 1、函数名不能发生改变
# 2、函数体内部代码不能发生改变
# def check(func):
#     def inner():
#         print("登录验证操作。。。")
#         func()
#     return inner
# @check
# def fss():
#     print("发说说")

# fss=check(fss)  #相当于变量名重新复制
def zhuangshiqi_line(func):
    def inner():
        print("--------------------------")
        func()
    return inner
def zhuangshiqi_star(func):
    def inner():
        print("*"*30)
        func()
    return inner
@zhuangshiqi_line
@zhuangshiqi_star
def print_content():
    print("人狠话不多")
print_content()
