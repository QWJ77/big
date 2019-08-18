'''
当我们写一个参数比较多的函数时，如果有些参数在大多数情况下都是某个固定值，
那么为了简化使用，就可以创建一个新函数，指定我们要使用的某个参数位固定值，
这个新函数就是偏函数
'''

def test(a,b,c,d=1):
    print(a+b+c+d)
#
# test(1,2,3)
#
#
# def test2(a,b,c=1,d=2):
#     test(a,b,c,d)
# test2(1,2,3)

# 比较麻烦

import functools
newfunc=functools.partial(test,c=5)
print(newfunc,type(newfunc))
newfunc(1,3)
#------------------------------ 场景-----------------------------
numStr="100010"
# result=int(numStr,base=2)
# print(result)
# 往后一段时间都需要把2进制字符串转换成10进制数据
int2=functools.partial(int,base=2)
print(int2(numStr))