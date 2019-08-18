#如果要用*，=装饰，则需要多个装饰器，麻烦，所以可以使用带参数的装饰器

def getzsq(char):
    def zsq(func):
        def inner():
            print(char * 30)
            func()
        return inner
    return zsq


@getzsq("*") #f1=zsq(f1),是没有办法改变的
def f1():
    print("666")

f1()
