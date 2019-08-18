'''
缺省参数：当我们使用一个函数的时候，如果大多数情况下，使用的某个数据是一个固定值
或者属于主功能之外的小功能的实现，则可以使用默认值，这种参数称为缺省参数
定义：def 函数名（变量名1=默认值1，变量值2=默认值2）
'''

result=sorted([1,2,4,5,3],reverse=True) #reverse=True缺省的情况是False升序，可不写
print(result)

# def hit(somebody="doudou"):
#     print("我想打",somebody)


def hit(somebody="doudou"):
    print("我想打",somebody)
hit()