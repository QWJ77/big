def zsq(func):
    def inner(*args,**kwargs):  #应当用不定长参数，因为使用装饰器的逻辑函数参数不确定参数个数
        print("-"*30)
        # func(args,kwargs)进行拆包
        func(*args,**kwargs)
    return inner   #返回一个新的函数给pnum
@zsq
def pnum(num,num2,num3):
    print(num,num2,num3)

@zsq
def pnum2(num):
    print(num)

pnum(1,2,num3=666)
pnum2(4)