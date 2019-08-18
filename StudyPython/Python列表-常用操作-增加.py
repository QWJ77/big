
# append 往列表里追加一个新元素,只追加一个元素
# 注意：会直接修改原列表!!!
# nums=[1,2,3,4,5]
# print(nums)
# print(nums.append(5))
# print(nums)

# insert(index,object) 插入到index的前面
# 它会改变列表本身!!!
# nums=[1,2,3,4,5]
# print(nums)
# print(nums.insert(0,5))
# print(nums)

# extend 往列表中。扩展另一个可迭代序列，把可迭代元素分解成每一个元素添加到列表
# 它会改变列表本身!!!

# nums=[1,2,3,4,5]
# # nums2=["a","b","c"]
# nums2="abcdefg"
# print(nums.extend(nums2))
# print(nums)

# 乘法运算
# 不会改变列表本身!!!
# nums=[1,2]
# print(nums*3)
# print([num *3 for num in nums])
# print(nums)

# 加法运算
# 只能连接链表到另一个列表，不能追加字符串，此处与extend不同
# 不会改变列表本身!!!
# n1=[1,2,3]
# n2=["a","b"]
# print(n1+n2)
# print(n1)