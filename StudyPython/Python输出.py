import sys
from time import sleep
# 输出一个值
# print(123)

# 输出一个变量
# num=55
# print(num)

# 输出多个变量
# num2=44
# print(num,num2)

# 格式化输出
# name=s='sa'
# age=18
# print("我是%s，今年%d"%(name,age))
# print("我是{0}，今年{1}".format(name,age))

# 输出到文件中
# f=open("test","w")
# 默认，标准输出输出到控制台
# print("xxxxxxx",file=f)
# print("xxxxxxx",file=sys.stdout)

# 输出不自送换行,end=什么就以什么结束，end默认=\n
# print("abc",end="\n")

# 输出各个数据，使用分隔符分割
# print("1","2",3,sep="&")

# flush参数说明,print打印时，先把内容放在缓冲区，再从缓冲区输出到控制台。如果内容里有\n（换行），会立刻输出到控制台
# 或者flush=True
# end参数默认是“\n”，

print("请输入账号", end=" ")


sleep(5)