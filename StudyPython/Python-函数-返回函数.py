'''
是指一个函数内部，返回的数据是另一个函数，把这样的操作称为返回函数
案例：根据不同参数，获取不同操作，做不同计算
'''
def getFunc(flag):
    # 1、再次定义几个函数
    def sum(a,b,c):
        return a+b+c
    def jian(a,b,c):
        return a-b-c
    # 2、根据不同flag值，返回不同操作函数
    if flag =="+":
        return sum
    elif flag == "-":
        return jian
result=getFunc("+")
# print(result,type(result))
res=result(1,3,5) #返回的result是sum，仍然是一个函数，所以可以调用它
print(res)
