# 有序可变的元素集合
# 方式一
# name=["arfer",True,[1,3]]
# 方式二
#----------------列表生成式--------------------
# 写一个1到99的列表
# num=range(99) 是0到98的列表
# nums=range(1,100)
# print(nums)
#----------------列表推导式--------------------
# 从一个list，推导出另一个list，映射解析
nums=[1,2,3,4,5]
# 原始方法
# resultlist=[]
# for num in nums:
#     # print(num)
#     if num%2==0:
#         continue
#     result=num**2
#     print(result)
#     resultlist.append(result)
# print(resultlist)

# 列表推导式
resultlist=[num **2 for num in nums if num%2!=0]
print(resultlist)
# resultlist=[num **2 for num in nums] [1,1,1,1,1]
