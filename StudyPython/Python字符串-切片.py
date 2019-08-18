name="abcdefg"
# print(name[2])
# print(name[-1])   #代表最后一个字符

print(name[0:3])  #前开后闭区间,取从0到2的所以
print(name[0:len(name):1])  #步长是1
# 步长不能够从头部跳到尾部
print(name[4:1:-1])
print(name[-1:-4:-1])
print(name[::-1]) #反转字符串