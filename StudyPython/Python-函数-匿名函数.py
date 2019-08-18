# 没有名字的函数
# lambda 参数1，参数2..:表达式

# result=(lambda x,y:x+y)(1,2)
# print(result)
#
# newFunc=lambda x,y:x+y
# print(newFunc(1,2))

l=[{"name":"sz","age":18},{"name":"sz2","age":19},{"name":"sz3","age":18.5}]
# def getKey(x):
#     return x["age"]
# 此函数用处很少
# result=sorted(l,key=getKey) #key参数接收函数
result=sorted(l,key=lambda x:x["age"])
print(result)