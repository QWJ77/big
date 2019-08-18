'''
当一个函数A的参数，接收的又是另一个函数时，则把这个函数A称为是“高阶函数”
'''

# 函数本身也可以作为数据传递给另外一个变量
# def test(a,b):
#     print(a+b)
# print(test)
# print(id(test))
# test2=test
# test2(1,4)

# sorted函数就是高阶函数
l=[{"name":"sz","age":18},{"name":"sz2","age":19},{"name":"sz3","age":18.5}]
def getKey(x):
    return x["age"]
result=sorted(l,key=getKey) #key参数接收函数
print(result)

def caculate(num1,num2,caculateFunc):
    print(caculateFunc(num1,num2))
def sum(a,b):
    return a+b
caculate(6,2,sum)
