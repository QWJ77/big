#当我们遇到某个函数，处理好数据之后，想要拿到处理的结果
#return
#注：return后续代码不会被执行
#只能返回一次
# 如果想返回多个数据，可以把多个数据包装成一个集合返回

# def mySum(a,b):
#     result=a+b
#     return result
#
# res=mySum(6,7)
# print(res)

# 计算两个数据和，差
def caculate(a,b):
    he=a+b
    cha=a-b
    return (he,cha)

res=caculate(6,7)
# print(res[0])
# print(res[1])
he,cha=res
print(he)
print(cha)