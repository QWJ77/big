#------------------------------ 判定--------------------------------
# 元素 in 列表
# 元素 not in 列表
# s="abc"
# print("a" in s)
# print("c" not in s)
#
# values=[1,2,3,4,5]
# print(5 in values)
# print(5 not in values)
#------------------------------ 比较--------------------------------
# cmp()内建函数，可以直接写出来，Python3不支持，直接用>,<,==

# ----------------------------- 排序--------------------------------
# sorted(iterable,key,reverse)返回一个排好序的列表，对所有可迭代对象进行排序
# iterable可迭代对象
# key排序关键字
# reverse=True降序
# 不改变列表本身!!!

s="acbegscv"
result=sorted(s,reverse=True)
print(result,s)

# s=[("sz",18),("sz1",16),("sz2",17),("sz3",15)] #按照整个元祖里的首个元素进行排序
# result=sorted(s)
# print(result)
# 想要按照指定key排序
# def getKey(x):
#     return x[1]
# result=sorted(s,key=getKey,reverse=True)
# print(result,s)

# 方式二，列表排序法，只能操作列表
# sort(key=None,reverse=False)
# 列表本身被改变,并没有把排序结果返回给外界，而是更改了对象本身!!!!!!
# l=[1,3,2,6,4,5]
# l=[("sz",18),("sz1",16),("sz2",17),("sz3",15)]
# def getKey(x):
#     return x[1]
# res=l.sort(key=getKey,reverse=True)
# print(res,l)

#-----------------------------------乱序和反转------------------------------------------
# 乱序，随机打乱一个序列
# 导入random模块，random.shuffle(list)
# 直接改变列表本身！！！
# import random
# l=[1,2,3,4,5]
# res=random.shuffle(l)
# print(l,res)

# 反转
# reverse()
# 直接改变列表本身！！！
# res=l.reverse()
# print(l,res)

# 切片反转，列表本身不会发生改变！！！
# res=l[::-1]
# print(res,l)

