# 交集
'''
intersection（Iterable）
Iterable是可遍历对象
字符串：只判定字符串中的非数字
列表
元组
字典
集合
逻辑与“&”一样

intersection_update()
交集计算完毕后会再次赋值给原对象（即交集），会更改原对象！！！
只适用于可变集合
用可变集合和不可变集合操作时，谁在前面就以谁的类型为准
'''
s1=frozenset([1,2,3,4,5])
s2={4,5,6}
# result=s1.intersection(s2)
# result=s1&s2
# result=s1.intersection_update(s2) #不可以，因为s1是不可变类型
result=s2.intersection_update(s1)
print(result,type(result))
print(s1,s2)#集合本身并没边
