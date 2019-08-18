#--------------------------字符串的填充--------------------------------------
# ljust
'''
根据指定字符（1个），将源字符串填充够指定长度
表示原字符串靠左,字符串本身没有发生改变
ljust(width,fillchar)
'''
# name='abc'
# print(name.ljust(6,'x'))

# rjust
'''
与ljust区别就是原字符串靠右
'''

# center
'''
表示原字符串居中，右边的补充字符比较多
'''
#--------------------------字符串的压缩--------------------------------------
# lstrip
'''
移除所有原字符串指定字符（默认为空白字符）
移除左侧的,从左侧第一位开始，第一位没有就不会走了
'''
# name=" wwwwwoo shi sz  "
# print("|"+name.lstrip()+"|")  #|wwwwwoo shi sz  |
# print("|"+name.lstrip("wo")+"|")
# print("|"+name+"|")

# rstrip
'''
移除所有原字符串指定字符（默认为空白字符）
移除右侧的,从右侧第一位开始，第一位没有就不会走了
'''

#----------------------------------字符串分割拼接-----------------------------------------
'''
split 将一个大字符串分割成几个子字符串
split(sep,maxsplit)
sep分隔符
maxaplit最大分割次数,省略则有多少分多少
返回分割后组成的“列表”
字符串本身并没有被改变！！！
'''
# info="sz-18-180-0660-432114"
# result=info.split("-",2)
# print(result)
# print(info)

'''
partition 根据指定的分隔符，返回（分隔符左侧内容，分隔符，分隔符右侧内容）三部分，从左边开始查找分隔符
如果没有查找到分隔符，返回（原字符串，"",""）
返回元祖类型
字符串本身并没有被改变！！！

'''
# info="sz-18-180-0660-432114"
# result=info.partition("-")
# print(result)
# print(info)

'''
rpartition 从右边开始查找分隔符

'''

'''
splitlines 按照换行符（\r,\n）,将字符串拆成多个元素，保存到列表中
语法
splitlines(keepends) keepends=True则保留分隔符
返回按换行度分割的多个字符串，作为元素组成的列表
'''
# info="wo\nshi\rsz"
# # result=info.splitlines()
# # print(result)
# print(info)

'''
join 根据给定字符串，将指定的可迭代对象，进行拼接，得到拼接后的字符串
join（iterable） iterable 可迭代的对象、字符串、元祖、列表
返回拼接后的字符串
'''
# items=["sz","18","shanghai"]
# result=",".join(items)
# print(result)
'''
isalpha 判断字符串中所有字符是否都是字母（大小写）
'''

'''
isdigit 判断字符串中所有字符是否都是数字
'''

'''
isalnum 判断字符串中所有字符是否都是数字或者字母
'''

'''
isspace 判断字符串中所有字符是否都是空白符
'''

'''
startswith 判断字符串是否以某个前缀开头
'''

'''
endswith 判断字符串是否以某某东西结束
'''

'''
in 判定一个字符串，是够被另一个字符串包含
'''

'''
not in 判定一个字符串，是否不被另一个字符串包含
'''