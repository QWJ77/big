# 带参数和返回值的装饰器的通用写法
def zsq(func):
    def inner(*args,**kwargs):
        print("-"*30)
        # func(args,kwargs)进行拆包
        res=func(*args,**kwargs)
        return res   #在func里返回逻辑函数的返回
    return inner   #返回一个新的函数给pnum
@zsq
def pnum(num,num2,num3):
    print(num,num2,num3)
    return num + num2 + num3

@zsq
def pnum2(num):
    print(num)

res1=pnum(1,2,num3=666)
res2=pnum2(4)
print(res1,res2)