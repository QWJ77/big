'''
装包：把传递的参数，包装成一个集合，称之为“装包”
拆包：把集合参数，再次分解成单独的个体，称之为“拆包”
'''

# def mySum(a,b,c,d):
#     print(a+b+c+d)
#
# def test(*args):
#     print(args)
# #     拆包
#     print(*args)
#     # mySum(args[0],args[1],args[2],args[3])  #麻烦
#     mySum(*args)
# test(1,2,3,4) #传递多个参数，进行装包

def mySum(a,b):
    print(a)
    print(b)

def test(**kwargs):
    print(kwargs)
#     拆包操作
#     使用两个**
#     print(**kwargs)  #无法直接打印
#     a=1,b=2
    mySum(**kwargs)
test(a=1,b=2)
