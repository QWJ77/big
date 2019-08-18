'''
定义变量的3中方式
方式一
a=2
b=3
方式二
a,b=2,2
方式三
a=b=3
'''
# score=input("请输入一个数字")
# print(int(score)+6)
# 整除和求余可以计算位置
# //取结果的整数部分
# a=10//3
# print(a)

# num=10
# print (id(num))

# ==比对的是值，is比对的是唯一表示，id
a=10
b=10
print(id(a),id(b))
print (a is b)

# a=[1]
# b=[1]
# print(a==b)  True
# print(id(a),id(b))
# print(a is b) False

# 支持链式比较运算符
# num=10
# print(5<num<20)


# 逻辑运算符
#not 非，取反,一元运算符
# b=True
# print( not b)

# 非0即真，非空即真！！
# print(11 or False)
# print(bool("0"))
# # 识别到哪个表达式就会把哪个表达式执行出来
# print(1 and 3)
# # 短路运算符
# print(1 or 3)
#
# print(0 or False or 6)