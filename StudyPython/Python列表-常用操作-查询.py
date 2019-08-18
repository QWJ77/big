'''
获取单个元素
'''
nums=range(10)
print(nums[5])#就是5

'''
获取元素索引
index(self, value, start=None, stop=None),从左到右进行查找，找到第一个就结束，可以通过限制区间进行查找
'''
index=nums.index(5)
print(index)

'''
获取指定元素个数
count(self, value)
'''
c=nums.count(5)
print(c)

'''
获取多个元素
切片 item[start:end:step] 前开后闭
'''
num1=[3,4,5,6,5,7,55,5,8,9]
pic=num1[::-1]  #字符串的反转
print(pic)